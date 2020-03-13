from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["pk","name","qualification"]
    list_filter = ["name","qualification"]
    list_display = [
        "pk",
        "name",
        "qualification",
        "contact",
        "email",
    ]
    
admin.site.register(Employee,EmployeeAdmin)
