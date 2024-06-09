# myportfolio/admin.py

from django.contrib import admin
from .models import Categoria, Tecnologia, Proyecto, Contacto

# Registro de modelos en el panel de administración
admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Proyecto)

#código etapa 3
admin.site.register(Contacto)