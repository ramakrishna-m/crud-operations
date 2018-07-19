from django.contrib import admin
from .models import Student

class StuAdmin(admin.ModelAdmin):
    list_display = ('Name','Mobile','Email','password','Gender','City','State')
admin.site.register(Student,StuAdmin)

