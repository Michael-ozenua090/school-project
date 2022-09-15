from django.shortcuts import render, redirect
from django.urls import reverse
from student.forms import StudentForm
from student.models import Student
from django.contrib import messages

# Create your views here.
def homepage(request):
    students = Student.objects.all()
    context = {
        'saved_student': students
    }
    return render(request, 'student/index.html', context)


def new_student(request):
    form = StudentForm(request.POST or None, request.FILES or None )
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('s_homepage'))
    return render(request, 'student/add_student.html', context)

def delete_student(request, id):
    students = Student.objects.get(id=id)
    students.delete()
    messages.success(request, 'Student info deleted')
    return redirect(reverse('s_homepage'))

def update_student(request, id):
    instance = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, 
                          request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Student Info Updated')
        return redirect(reverse('s_homepage'))
    return render(request, 'student/update_student.html', context)
