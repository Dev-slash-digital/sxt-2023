#!/usr/bin/env python
"""
Script de prueba para enviar un email usando MAILDRILL
Uso: python test_email.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sxt_2023.django.settings')
django.setup()

from smtplib import SMTPException

from sxt_2023.apps.people.models import User
from wailer.models import Email


def send_test_email():
    """Envía un email de prueba a una lista de correos."""
    
    emails = [
        "jean.martial@slash-experience.com",
        "david.ortiz@slash-digital.io",
        "paypal.trabajalatino@gmail.com",
    ]

    for email in emails:
        try:
            user = User.objects.get(email=email)
            brand = user.registration_brand
            address = brand.postal_address if brand else "Dirección no especificada"
            brand_name = brand.name if brand else "SXT"

            print(f"Enviando correo a {email} para la marca {brand_name}...")
            Email.send(
                "registration_confirmation",
                {
                    "brand": brand_name,
                    "address": address,
                    "email": email,
                    "locale": "es",
                },
            )
            print(f"Correo enviado exitosamente a {email}")

        except User.DoesNotExist:
            print(f"Usuario con email {email} no encontrado. Saltando...")
        except SMTPException as e:
            print(f"Error al enviar correo a {email}: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado con {email}: {e}")


if __name__ == "__main__":
    send_test_email()
