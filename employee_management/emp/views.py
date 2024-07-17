from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee,Gallery
import re
from django.core.exceptions import ValidationError
# Create your views here.

def validate_phone_number(value):
    if not re.fullmatch(r'\d{10}', value):
        raise ValidationError('Invalid phone number')
    
def home(request):
    emps = Employee.objects.all()
    return render(request,'home.html',{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        # Fetch the data
        emp_id = request.POST.get('emp-id')
        emp_name = request.POST.get('emp-name')
        emp_address = request.POST.get('emp-address')
        emp_phone = request.POST.get('emp-phone')
        emp_department = request.POST.get('emp-department')
        emp_working = request.POST.get('emp-working')
        # create model object and set the data
        e = Employee()
        e.emp_id =emp_id
        e.name =emp_name
        e.address =emp_address
        # e.phone =emp_phone
        e.department = emp_department
        e.working =emp_working
        
        try:
            validate_phone_number(emp_phone)
            e.phone=emp_phone
        except ValidationError as e:
            return HttpResponse(f'Error: {e.message}')
        
        if emp_working is None:
            e.working = False
        else:
            e.working = True
    
        # save the object
        e.save()
        
        # prepare msg
        return redirect('/')
    return render(request,'add_emp.html',{})

def view_emp(request):
    return render(request,'home.html',{})


def delete_emp(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/')


def update_emp(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    return render(request,'update_emp.html',{'emp':emp})


def do_update_emp(request,emp_id):
    
    if request.method=="POST":
        # Fetch the data
        emp_id_temp = request.POST.get('emp-id')
        emp_name = request.POST.get('emp-name')
        emp_address = request.POST.get('emp-address')
        emp_phone = request.POST.get('emp-phone')
        emp_department = request.POST.get('emp-department')
        emp_working = request.POST.get('emp-working')
        
        e = Employee.objects.get(pk=emp_id)
        e.emp_id = emp_id_temp
        e.name = emp_name
        e.address = emp_address
        e.phone = emp_phone
        e.department = emp_department
        e.working = emp_working
        
        try:
            validate_phone_number(e.phone)
            e.phone=e.phone
        except ValidationError as e:
            return HttpResponse(f'Error: {e.message}')
        
        if emp_working is None:
            e.working = False
        else:
            e.working = True
            
        e.save()
        
        # prepare msg
    return redirect('/')


def gallery(request):
    gallery_objs = Gallery.objects.all()
    return render(request,'gallery.html',{"gallery_objs":gallery_objs})