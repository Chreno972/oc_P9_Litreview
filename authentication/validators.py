"""validators module"""
from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    """ ContainsLetterValidator class """

    def validate(self, password, user=None):  # pylint: disable=unused-argument
        """_summary_: validate method

        Args:
            password (_type_): _description_

        Raises:
            ValidationError: _description_
        """
        if not any(char.isalpha() for char in password):
            # sinon, on lève une exception
            raise ValidationError(
                "Le mot de passe doit contenir une lettre",
                code="password_no_letters",
            )

    # retourne une chaine de caractère qui guide l'utilisateur
    def get_help_text(self):
        """ get_help_text method """
        return "Ajoutez une lettre majuscule ou minuscule."


class ContainsNumberValidator:
    """ ContainsNumberValidator class """
    def validate(self, password, user=None):  # pylint: disable=unused-argument
        """_summary_: validate method

        Args:
            password (_type_): _description_

        Raises:
            ValidationError: _description_
        """
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                "Le mot de passe doit contenir un chiffre",
                code="password_no_number",
            )

    def get_help_text(self):
        """ get_help_text method """

        return "Votre mot de passe doit contenir au moins un chiffre."
