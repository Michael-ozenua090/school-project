from django.shortcuts import render, redirect
from django.urls import reverse
from department.models import Department
from django.contrib import messages

from department.forms import DepartmentForm

# Create your views here.
def homepage(request):
    departments = Department.objects.all()
    context = {
        'saved_dept': departments
    }
    return render(request, 'department/index.html', context)


def add_dept(request):
    form = DepartmentForm(request.POST or None, request.FILES or None )
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('d_homepage'))
    return render(request, 'department/add_dept.html', context)

def delete_dept(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.success(request, 'Department Deleted')
    return redirect(reverse('d_homepage'))

def update_dept(request, id):
    instance = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None, 
                          request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Department Updated')
        return redirect(reverse('d_homepage'))
    return render(request, 'department/update_dept.html', context)