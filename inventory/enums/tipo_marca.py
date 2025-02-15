from django.utils.translation import gettext_lazy as _

class TipoMarca:
    DELL = 'A'
    LENOVO = 'B'
    HP = 'C'
    ASUS = 'D'
    OTROS = 'E'

    OPCIONES = [
        (DELL, _('DELL')),
        (LENOVO, _('LENOVO')),
        (HP, _('HP')),
        (ASUS, _('ASUS')),
        (OTROS, _('OTROS')),

    ]