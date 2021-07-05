from django.contrib import admin
from .models import Categoria, Libro, Contacto
from .forms import ProductoForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]
    list_per_page = 5
    form = ProductoForm

admin.site.register(Categoria)
admin.site.register(Libro, ProductoAdmin) 
admin.site.register(Contacto)

