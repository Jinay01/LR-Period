from django.contrib import admin

# Register your models here.

from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(College)
admin.site.register(Stream)

# STUDENTS


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'college_name', 'stream_name')


admin.site.register(Student, StudentAdmin)

# COMMITTEE


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['committee_name', 'college_name']


admin.site.register(Committee, CommitteeAdmin)
