#!/usr/bin/env python
"""
Script de prueba para enviar un email usando MAILDRILL
Uso: python test_email.py
"""

import os
import django
import traceback

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sxt_2023.django.settings')
django.setup()

from smtplib import SMTPException

from sxt_2023.apps.people.models import User
from wailer.models import Email


def send_test_email():
    """Envía un email de prueba a una lista de correos."""
    
    emails = [
        "Xavierbll@gmail.com",
        "agilaguirre@hotmail.com",
        "jean.martial@slash-experience.com",
        "belen.mayor@indop.net",
        "yarayjuan@telefonica.net",
        "beatriz.fillol@gmail.com",
        "mmateoslindemann@gmail.com",
        "isabelr_me@yahoo.es",
        "claudia.anayalopez@gmail.com",
        "jean.martial@protonmail.com",
        "elijimsan2407@gmail.com",
        "Susana.correa@abanca.com",
        "jean.martial+1@slash-digital.io",
        "martialjm@gmail.com",
        "acmahou@gmail.com",
        "bbs2612@gmail.com",
        "cpvazquez@telefonica.net",
        "beatriz.soler@esade.edu",
        "geni1955@hotmail.com",
        "angelapv1964@gmail.com",
        "monicalobosanz@gmail.com",
        "veronica@verili.es",
        "sofia@grigny.es",
        "rosario.cabane@icloud.com",
        "mlobolm@gmail.com",
        "alejandra.galobart@gmail.vom",
        "juanrhb@hotmail.com",
        "mariacorsinim@gmail.com",
        "ana@analopez.net",
        "e.martinmerino@gmail.com",
        "maria1antolin@yajoo.com",
        "fernandajcs@icloud.com",
        "acobo@adrianacobo.net",
        "72estebanelena@gmail.com",
        "elcomun02@hotmail.com",
        "martialjm+545@gmail.com",
        "pclcontreras@gmail.com",
        "maite.gomezgil@gmail.com",
        "bdcm73@me.com",
        "rinconelena@hotmail.com",
        "escobarcb75@yahoo.com",
        "isabelpascualdequinto@gmail.com",
        "patriciadecara@hotmail.com",
        "auratm@hotmail.com",
        "pilarmartinbr@gmail.com",
        "carmegras@gmail.com",
        "nereamca@hotmail.com",
        "veraguerra18@yahoo.com",
        "allexalvarezaznar@gmail.com",
        "ursulalv@gmail.com",
        "susana60@hotmail.com",
        "paloma.onate@ie.edu",
        "ipresmanes@hotmail.com",
        "conchitaamell@aol.com",
        "a.pernas@btinternet.com",
        "barbarapmanzarbeitia@gmail.com",
        "solete.silva@gmail.com",
        "idoiaarroyo@gmail.com",
        "valeriamoragues@gmail.com",
        "begoaalva@yahoo.es",
        "margotaraujog@gmail.com",
        "marionacolomer2960@hotmail.com",
        "bordovas@christies.com",
        "evafs72@gmail.com",
        "mariateencuentracasa@hotmail.es",
        "kgregory@kannavalley.com",
        "ainhoa.grino@es.swatchgroup.com",
        "cotecalbeto@telefonica.net",
        "mercedes@browniespain.com",
        "ana.segui.eguillor@gmail.com",
        "elinm16@yahoo.com",
        "clanzarot@madridbarriodesalamanca.com",
        "bmarquinas@gmail.com",
        "duquedeteruel@gmail.com",
        "beticharlan@hotmail.com",
        "tcv@gruporml.com.mx",
        "nieves@nievesalvarez.com",
        "alifreireva@gmail.com",
        "claudiae10@hotmail.es",
        "claudiae26@hotmail.com",
        "rociofuertes@roemi.es",
        "gabrielafontquer@gmail.com",
        "albadocampocadavid5@gmail.com",
        "bethgj@gmail.com",
        "vvlvidal@hotmail.com",
        "elenafragamonsalve@gmail.com",
        "maribelfuertes@roemi.es",
        "m.peccini@todsgroup.com",
        "radamantiz.do2017@gmail.com",
        "jean.martial@slash-digital.io",
        "remediosleonplaza@gmail.com",
        "mcampoymarquez@gmail.com",
        "robdimauro@gmail.com",
        "casilda.delaplaza@cartier.com",
        "casdelaplaza94@hotmail.com",
        "paulo26062012@gmail.com",
        "fjlopez@tecwork.es",
        "delamataeva@gmail.com",
        "marketilloss@gmail.com",
        "nikitashenja@gmail.com",
        "cardenas9559@gmail.com",
        "ebb1609200@outlook.es",
        "rojo666_007@hotmail.com",
        "victor.abad@jaeger-lecoultre.com",
        "swiwelfjc@gmail.com",
        "i.fernandez@sayma.es",
        "francisco.lozano@stefanoricci.com",
        "pilar.satrustegui@jaeger-lecoultre.com",
        "ollantaycastillo@gmail.com",
        "layla.li@jaeger-lecoultre.com",
        "marianela.ruiz@jaeger-lecoultre.com",
        "carla_perezalbarran@loewe.com",
        "malu.celemin@gmail.com",
        "carlota.sansalvador@jaeger.lecoultre.com",
        "david.ortiz@slash-digital.io",
        "david.or2018@gmail.com",
    ]

    for email in emails:
        try:
            user = User.objects.get(email__iexact=email)
            brand = user.registration_brand
            address = brand.postal_address if brand else "Dirección no especificada"
            brand_name = brand.name if brand else "SXT"

            print(f"Enviando correo a {email} para la marca {brand_name}...")
            Email.send(
                "registration",
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
            print(f"Ocurrió un error de SMTP con {email}: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado con {email}:")
            traceback.print_exc()


if __name__ == "__main__":
    send_test_email()
