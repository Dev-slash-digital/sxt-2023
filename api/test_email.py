#!/usr/bin/env python
"""
Script de prueba para enviar un email usando Wailer
Uso: python test_email.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sxt_2023.django.settings')
django.setup()

from wailer.models import Email


def send_test_email():
    """Envía un email de prueba a david.ortiz@slash-digital.io"""
    
    print("🚀 Enviando email de prueba...")
    print(f"📧 Destinatario: david.ortiz@slash-digital.io")
    print(f"📝 Tipo: registration")
    
    try:
        # Enviar email de registro de prueba
        Email.send(
            "registration",
            {
                "email": "david.ortiz@slash-digital.io",
                "locale": "es",
                "brand": "Test Brand",
                "address": "Calle Test 123, Madrid",
            },
        )
        
        print("✅ Email enviado exitosamente!")
        print("\n📊 Verifica:")
        print("   1. Tu bandeja de entrada en david.ortiz@slash-digital.io")
        print("   2. La carpeta de spam")
        print("   3. Los logs de Mailgun en https://app.mailgun.com/")
        
    except Exception as e:
        print(f"❌ Error al enviar email: {e}")
        print("\n🔍 Verifica:")
        print("   1. Que el API key de Mailgun sea correcto")
        print("   2. Que el dominio esté verificado en Mailgun")
        print("   3. Que las dependencias estén instaladas (wailer, anymail)")
        raise


if __name__ == "__main__":
    send_test_email()
