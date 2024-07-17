from django.contrib import admin
from .models import Employee,Gallery
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('emp_id','name','address','phone','department','working')

class GalleryAdmin(admin.ModelAdmin):
    list_display=('uploadedby','image','stars')

admin.site.register(Employee,EmpAdmin)
admin.site.register(Gallery,GalleryAdmin)