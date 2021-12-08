from django.contrib import admin
from .models import *



# Register your models here.
admin.site.site_header='TCC A+ Admin'
admin.site.index_title ='Welcome Admin'

class Studentuser(admin.ModelAdmin):
    list_display = ['user','course', 'section']
    search_fields =  ['course', 'section']

class Teacheruser(admin.ModelAdmin):
    list_display = [ 'user','department', 'user_image']
    search_fields =  ['department']

class sg(admin.ModelAdmin):
    list_display = ['subject', 'student', 'teacher', 'user_grade' ]
    search_fields =  ['subject', 'student', 'teacher']

admin.site.register(Student, Studentuser)
admin.site.register(Teacher, Teacheruser)
admin.site.register(Subjects, sg)