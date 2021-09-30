from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Child
from .models import Department
from .models import Coordinator
from .models import Volunteer
from .models import VolunteerReport
from .models import Mapping


class CoordinatorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'status', 'updated_at')
    list_filter = ('last_name', 'status')
    search_fields = ['last_name', 'first_name']


admin.site.register(Coordinator, CoordinatorAdmin)


class VolunteerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'status', 'updated_at')
    list_filter = ('last_name', 'status')
    search_fields = ['last_name', 'first_name']


admin.site.register(Volunteer, VolunteerAdmin)


class MappingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('department', 'coordinator', 'volunteer', 'date_completed')
    list_filter = ('department', 'coordinator', 'volunteer')


admin.site.register(Mapping, MappingAdmin)


class VolunteerReportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('volunteer', 'completed', 'date_completed', 'satisfaction')
    list_filter = ('volunteer', 'completed', 'satisfaction')


admin.site.register(VolunteerReport, VolunteerReportAdmin)


class ChildAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('child_code', 'status', 'created_at', 'updated_at')
    list_filter = ('child_code', 'status')
    search_fields = ['child_code']


admin.site.register(Child, ChildAdmin)


class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'city', 'email', 'phone')
    search_fields = ['name', 'city']


admin.site.register(Department, DepartmentAdmin)
