from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta

from .models import Brand, Visit, InvitationsStats, TreeVisitsMatrix, TreeScansStats

# Register your models here.


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_per_page = 1000
    list_max_show_all = 10000
    list_display = ("email", "registration_brand", "visits_count", "date_joined")
    list_filter = ("registration_brand", "date_joined")
    list_select_related = ["registration_brand"]


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "postal_address", "registration_url", "tree_url", "total_users", "total_visits")


class VisitAdmin(admin.ModelAdmin):
    list_per_page = 1000
    list_max_show_all = 10000
    list_display = ("user", "brand", "visited_at")
    list_filter = ("brand", "visited_at") 


class InvitationsStatsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def changelist_view(self, request, extra_context=None):
        # Get filter parameters
        filter_type = request.GET.get('filter', 'all')
        date_from = request.GET.get('date_from', '')
        date_to = request.GET.get('date_to', '')
        
        # Build query
        queryset = User.objects.all()
        
        # Apply date filters
        if filter_type == 'today':
            today = timezone.now().date()
            queryset = queryset.filter(date_joined__date=today)
        elif filter_type == 'custom' and date_from and date_to:
            queryset = queryset.filter(
                date_joined__date__gte=datetime.strptime(date_from, '%Y-%m-%d').date(),
                date_joined__date__lte=datetime.strptime(date_to, '%Y-%m-%d').date()
            )
        
        # Aggregate data
        stats = queryset.values('registration_brand__name').annotate(
            total=Count('id')
        ).order_by('-total')
        
        # Calculate total
        total_registrations = sum(item['total'] for item in stats)
        
        context = {
            **self.admin_site.each_context(request),
            'stats': stats,
            'total': total_registrations,
            'filter_type': filter_type,
            'date_from': date_from,
            'date_to': date_to,
        }
        
        return render(request, 'admin/invitations_stats.html', context)


class TreeVisitsMatrixAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def changelist_view(self, request, extra_context=None):
        # Get filter parameters
        filter_type = request.GET.get('filter', 'all')
        date_from = request.GET.get('date_from', '')
        date_to = request.GET.get('date_to', '')
        
        # Build query
        queryset = Visit.objects.select_related('brand', 'user__registration_brand')
        
        # Apply date filters
        if filter_type == 'today':
            today = timezone.now().date()
            queryset = queryset.filter(visited_at__date=today)
        elif filter_type == 'custom' and date_from and date_to:
            queryset = queryset.filter(
                visited_at__date__gte=datetime.strptime(date_from, '%Y-%m-%d').date(),
                visited_at__date__lte=datetime.strptime(date_to, '%Y-%m-%d').date()
            )
        
        # Get all brands
        all_brands = Brand.objects.all().order_by('name')
        
        # Build matrix data
        matrix = {}
        row_totals = {}
        col_totals = {}
        
        for visit in queryset:
            tree_brand = visit.brand.name
            user_brand = visit.user.registration_brand.name if visit.user.registration_brand else "Sin marca"
            
            if tree_brand not in matrix:
                matrix[tree_brand] = {}
                row_totals[tree_brand] = 0
            
            if user_brand not in matrix[tree_brand]:
                matrix[tree_brand][user_brand] = 0
            
            matrix[tree_brand][user_brand] += 1
            row_totals[tree_brand] += 1
            
            if user_brand not in col_totals:
                col_totals[user_brand] = 0
            col_totals[user_brand] += 1
        
        # Get unique user brands (columns)
        user_brands = sorted(set(
            visit.user.registration_brand.name if visit.user.registration_brand else "Sin marca"
            for visit in queryset
        ))
        
        # Build rows for template
        matrix_rows = []
        for brand in all_brands:
            if brand.name in matrix:
                row = {
                    'tree_brand': brand.name,
                    'values': [matrix[brand.name].get(ub, 0) for ub in user_brands],
                    'total': row_totals[brand.name]
                }
                matrix_rows.append(row)
        
        # Calculate grand total
        grand_total = sum(row_totals.values())
        
        context = {
            **self.admin_site.each_context(request),
            'user_brands': user_brands,
            'matrix_rows': matrix_rows,
            'col_totals': [col_totals.get(ub, 0) for ub in user_brands],
            'grand_total': grand_total,
            'filter_type': filter_type,
            'date_from': date_from,
            'date_to': date_to,
        }
        
        return render(request, 'admin/tree_visits_matrix.html', context)


class TreeScansStatsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def changelist_view(self, request, extra_context=None):
        from .models import TreePageView
        from django.contrib import messages
        from django.http import HttpResponseRedirect
        
        # Handle clear data action
        if request.method == 'POST' and 'clear_data' in request.POST:
            count = TreePageView.objects.all().count()
            TreePageView.objects.all().delete()
            messages.success(request, f'Successfully deleted {count} tree scan records.')
            return HttpResponseRedirect(request.path)
        
        # Get filter parameters
        filter_type = request.GET.get('filter', 'all')
        date_from = request.GET.get('date_from', '')
        date_to = request.GET.get('date_to', '')
        
        # Build query
        queryset = TreePageView.objects.select_related('brand')
        
        # Apply date filters
        if filter_type == 'today':
            today = timezone.now().date()
            queryset = queryset.filter(viewed_at__date=today)
        elif filter_type == 'custom' and date_from and date_to:
            queryset = queryset.filter(
                viewed_at__date__gte=datetime.strptime(date_from, '%Y-%m-%d').date(),
                viewed_at__date__lte=datetime.strptime(date_to, '%Y-%m-%d').date()
            )
        
        # Aggregate data
        stats = queryset.values(
            'brand__name',
            'brand__postal_address'
        ).annotate(
            total=Count('id')
        ).order_by('-total')
        
        # Calculate total
        total_scans = sum(item['total'] for item in stats)
        total_records = TreePageView.objects.count()
        
        context = {
            **self.admin_site.each_context(request),
            'stats': stats,
            'total': total_scans,
            'total_records': total_records,
            'filter_type': filter_type,
            'date_from': date_from,
            'date_to': date_to,
        }
        
        return render(request, 'admin/tree_scans_stats.html', context)


admin.site.register(User, UserAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(InvitationsStats, InvitationsStatsAdmin)
admin.site.register(TreeVisitsMatrix, TreeVisitsMatrixAdmin)
admin.site.register(TreeScansStats, TreeScansStatsAdmin)
