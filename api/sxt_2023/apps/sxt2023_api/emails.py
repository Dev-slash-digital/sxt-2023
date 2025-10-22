from typing import Mapping

from wailer.interfaces import EmailType, JsonType


class Registration(EmailType):
    def get_to(self) -> str:
        return self.data["email"]

    def get_locale(self) -> str:
        return self.data["locale"]

    def get_context(self) -> Mapping[str, JsonType]:
        return dict(
            brand=self.data["brand"],
            address=self.data["address"],
            email=self.data["email"],
        )

    def get_subject(self) -> str:
        return "Ruta Solidarity Xmas Tree - Confirmación de registro"

    def get_template_html_path(self) -> str:
        return "mails/registration.html"

    def get_template_text_path(self) -> str:
        return "mails/registration.html"


class RaffleConfirmation(EmailType):
    def get_to(self) -> str:
        return self.data["email"]

    def get_locale(self) -> str:
        return self.data["locale"]

    def get_context(self) -> Mapping[str, JsonType]:
        return dict()

    def get_subject(self) -> str:
        return "Ruta Solidarity Xmas Tree - Confirmación del sorteo"

    def get_template_html_path(self) -> str:
        return "mails/raffle.html"

    def get_template_text_path(self) -> str:
        return "mails/raffle.html"
