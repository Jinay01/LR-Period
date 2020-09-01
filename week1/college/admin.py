from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(College)
admin.site.register(Stream)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'college_name', 'stream_name')


admin.site.register(Student, StudentAdmin)
