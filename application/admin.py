from django.contrib import admin
from .models import Department, Employee, EmployeeRole, Record


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'department_name')
    search_fields = ('^department_name',)
    list_filter = ('department_name',)


class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'role')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'employee', 'employee_department', 'employee_role')
    search_fields = ('^employee',)
    list_filter = ('employee_department',)


class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'applicant_name',
        'position',
        'department',
        'interview_date',
        'time_to_complete',
        'name_hr',
        'position_hr',
        'date_of_get',
        'head_of_department_name'
    )
    search_fields = ('^applicant_name',)
    list_filter = ('position', 'department', 'interview_date')
    empty_value_display = 'поле не заполнено'


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeRole, EmployeeRoleAdmin)
admin.site.register(Record, RecordAdmin)
