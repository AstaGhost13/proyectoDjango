from django.contrib import admin

# Register your models here.
from .models import Floor, Department, Position, Custodiam


class FloorAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'status', 'description')
    search_fields = ('pkid', 'id',  'status', 'description')
    list_filter = ('pkid', 'id',  'status', 'description')


admin.site.register(Floor, FloorAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'id_floor', 'status', 'description','parent')
    search_fields = ('pkid', 'id', 'id_floor', 'status', 'description','parent')
    list_filter = ('pkid', 'id', 'id_floor', 'status', 'description','parent')


admin.site.register(Department, DepartmentAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'description', 'status', 'department')
    search_fields = ('pkid','description', 'department__description')
    list_filter = ('pkid','id', 'department')

admin.site.register(Position, PositionAdmin)


class CustodiamAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'position', 'first_name', 'last_name' , 'reference') 
    search_fields = ('pkid', 'position', 'first_name', 'last_name')  
    list_filter = ('status', 'position', 'created_at')  

admin.site.register(Custodiam, CustodiamAdmin)