# Plan de Implementación - Dashboards de Estadísticas en Admin

- [ ] 1. Crear modelo TreePageView para tracking de URLs de escaneo
- [x] 1.1 Agregar modelo TreePageView en models.py


  - Campos: tree_id (UUID), brand (FK a Brand), viewed_at (DateTimeField con auto_now_add)
  - _Requerimientos: 4.1, 4.2, 4.3_

- [x] 1.2 Crear migración para TreePageView


  - Ejecutar makemigrations para generar la migración
  - _Requerimientos: 4.1_

- [ ] 2. Implementar tracking en la vista de escaneo
- [x] 2.1 Modificar vista visit_tree en views.py


  - Al inicio de la función, crear registro TreePageView con tree_id y brand
  - _Requerimientos: 4.2, 4.3, 4.9_

- [ ] 3. Crear modelos proxy para las 3 tablas estadísticas
- [x] 3.1 Crear modelo proxy InvitationsStats en models.py


  - Proxy de User con Meta: proxy=True, verbose_name
  - _Requerimientos: 2.1_

- [x] 3.2 Crear modelo proxy TreeVisitsMatrix en models.py

  - Proxy de Visit con Meta: proxy=True, verbose_name
  - _Requerimientos: 3.1_

- [x] 3.3 Crear modelo proxy TreeScansStats en models.py

  - Proxy de TreePageView con Meta: proxy=True, verbose_name
  - _Requerimientos: 4.4_

- [ ] 4. Implementar AdminModels con vistas personalizadas
- [x] 4.1 Crear InvitationsStatsAdmin en admin.py


  - Sobrescribir changelist_view para mostrar tabla personalizada
  - Implementar filtros de fecha: Hoy, Todo, Rango personalizado
  - Query: User.objects.values('registration_brand__name').annotate(count=Count('id'))
  - Renderizar template simple con tabla HTML
  - _Requerimientos: 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.2, 2.3, 2.4, 2.5_

- [x] 4.2 Crear TreeVisitsMatrixAdmin en admin.py


  - Sobrescribir changelist_view para mostrar matriz personalizada
  - Implementar filtros de fecha
  - Query: Visit.objects con agregaciones para crear matriz marca_arbol x marca_usuario
  - Renderizar template con tabla matriz HTML
  - _Requerimientos: 1.1, 1.2, 1.3, 1.4, 1.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6_

- [x] 4.3 Crear TreeScansStatsAdmin en admin.py



  - Sobrescribir changelist_view para mostrar tabla personalizada
  - Implementar filtros de fecha
  - Query: TreePageView.objects.values('brand__name').annotate(count=Count('id'))
  - Renderizar template simple con tabla HTML
  - _Requerimientos: 1.1, 1.2, 1.3, 1.4, 1.5, 4.4, 4.5, 4.6, 4.7, 4.8_

- [ ] 5. Registrar los modelos proxy en admin.py
- [x] 5.1 Registrar InvitationsStats con InvitationsStatsAdmin

  - admin.site.register(InvitationsStats, InvitationsStatsAdmin)
  - _Requerimientos: 2.1_

- [x] 5.2 Registrar TreeVisitsMatrix con TreeVisitsMatrixAdmin

  - admin.site.register(TreeVisitsMatrix, TreeVisitsMatrixAdmin)
  - _Requerimientos: 3.1_

- [x] 5.3 Registrar TreeScansStats con TreeScansStatsAdmin


  - admin.site.register(TreeScansStats, TreeScansStatsAdmin)
  - _Requerimientos: 4.4_
