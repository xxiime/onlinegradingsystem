from django.db import models
#dagdag
from django.contrib.auth.models import User
# from django.db.models.fields.related import RelatedField
from datetime import datetime
import os, random

from django.utils import timezone
from django.utils.html import mark_safe

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars ='ABCDEFGHIJKLMNOPQRSTUVWXZYabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr =''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid = instance, basename =basefilename, randomstring = randomstr, ext=file_extension, year=_now.strftime('%Y'), month = _now.strftime('%m'), day =_now.strftime('%d'))


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False) #null=True,
    course = models.CharField(max_length=255, null=True, blank=False)
    section = models.CharField(max_length=255, null=True, blank=False)
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/default.jpg')

    def __str__(self):
        return self.user.id

    def image_tag(self):
        return mark_safe('<img src="/Aplus/fileupload/%s" width="50" height="50" />'%(self.user_image))

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False) #null=True,
    department = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/default.jpg')

    def __str__(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img src="/Aplus/fileupload/%s" width="50" height="50" />'%(self.user_image))

def exclfile_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars ='ABCDEFGHIJKLMNOPQRSTUVWXZYabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr =''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'gradesheet/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid = instance, basename =basefilename, randomstring = randomstr, ext=file_extension, year=_now.strftime('%Y'), month = _now.strftime('%m'), day =_now.strftime('%d'))

class Subjects(models.Model):
    subject = models.CharField(max_length=20)
    user_grade = models.FileField(upload_to=exclfile_path, null=True, default=None)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
    