from django.contrib import admin
from emp_app.models import employee,role,department

# Register your models here.

admin.site.register(employee)
admin.site.register(role)
admin.site.register(department)