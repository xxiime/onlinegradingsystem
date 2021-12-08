from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from Aplus.models import Student, Subjects, Teacher
from .forms import LoginForm #,SignUpForm
from django.contrib.auth import authenticate, login, logout
# from Aplus.models import *

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg':msg})

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if Student.objects.filter(user=request.user).exists():
        student = Student.objects.get(user=request.user.id)
        subject = Subjects.objects.select_related('student').filter(student_id=student)
        # dsubject = subject.distinct('subject')
        return render(request, "home.html", context={"student": student, 'subject':subject})

    elif Teacher.objects.filter(user=request.user).exists():
        teacher = Teacher.objects.get(user=request.user.id)
        subject = Subjects.objects.select_related('teacher').filter(teacher_id=teacher)
        # student = User.objects.get(id=subject.student.user_id)
        return render(request, "teacherhome.html", context={"teacher": teacher, 'subject':subject})
    
    # teacher = Teacher.objects.filter(user=request.user).select_related()
    # if not student.exists():
    #     return redirect("login")

    # if student.ex :
    #     subject = Subjects.objects.all().filter(student.user_id)
    #     return render(request, "home.html", context={"student": student, 'subject':subject})
    # else:
    #     return render(request, "home.html", context={"teacher": teacher.first()})
        

def logout_view(request):
    logout(request)
    return redirect('login_view')

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            User = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})
    
# def say_hello(request):
#     return render(request, 'hello.html', {'name': 'mi'})

import openpyxl
import xlwings as xw

def grading(request, user_grading):
    try:
        grade = Subjects.objects.get(id=user_grading)
        # wb = openpyxl.load_workbook(grade.user_grade, data_only=True)
        # ws = wb['grading']
        # rows = ws.iter_rows()

       
        wb = xw.Book('fileupload/'+ str(grade.user_grade))
        wb.visible = False
        ws = wb.sheets[0]
        rows = ws.range("A1:G3").value

        mydict = {
            'grade':grade,
            'rows':rows,
        }
        
    except User.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'grading.html', context=mydict)

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, reverse
import os


def excelupdate(request, gradeid):
    if request.GET:
        grade = Subjects.objects.get(id=gradeid)
        subject = Subjects.objects.select_related('teacher').filter(teacher_id=grade.teacher)
        
        
        wb = xw.Book('fileupload/'+ str(grade.user_grade))
        wb.visible = False
        ws = wb.sheets['grading']
        rows = ws.range("A1:G3").value
        # rows = ws.range("A1").expand().value
        for index, row in enumerate(rows, start=1):
            if index!=1:
                for i, cells in enumerate(row, start=1):
                    if i!=1:
                        val = request.GET.get(str(index)+str(i))
                        print(str(index)+str(i))
                        if isinstance(val, (int, float)):
                            ws.cells(index, i).value = int(val)
                        else:
                            trnslt = (str(val))
                            ws.cells(index, i).value = trnslt
        wb.save()
   
        

    
        return render(request, 'teacherhome.html', {'grade':grade, 'subject':subject})
        