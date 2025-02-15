
from django.utils.translation import gettext_lazy as _



class TipoDisco:
    MECANICO = 'A'
    SOLIDO = 'B'
    
    OPCIONES = [
        (MECANICO, _('MECANICO')),
        (SOLIDO, _('SOLIDO')),
        
    ]


