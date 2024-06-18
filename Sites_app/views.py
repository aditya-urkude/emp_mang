from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from .models import *


def home(request):
    dp_objs = Department.objects.all()
    emp_objs = Employee.objects.all()
    error=""
    print("home")
    if request.method =='POST':

        form_type = request.POST.get('form_type')
        print("formtype = ",form_type)
        if form_type == 'emp_form':
            n = request.POST['Employee']
            e = request.POST['Email']
            m = request.POST['Mobile']
            dt = request.POST['Dept_type']
            a = request.POST['Address']
            db = request.POST['DOB']
            dj = request.POST['DOJ']
            gdr = request.POST['Gender']

            print(n, e, m , dt, a, db, dj, gdr)
            u = Department.objects.filter(dept_name=dt).first() 
            try:
                Employee.objects.create(emp_name = n,address= a,mobile=m,email=e, dob=db,doj=dj,gender=gdr,dept_id=u)
                error="no"
            except:
                error="yes"
            return render(request, 'home.html',locals())
        print("error ",error)
        
        if form_type == 'dept_form':
            return create_dept(request,error,dp_objs,emp_objs)
  
    return render(request,'home.html',{'dp_objs': dp_objs, 'error': error, 'emp_objs':emp_objs})

def create_dept(request, error,dp_objs,emp_objs):
    print("create dept")
    if request.method=='POST':
        dn = request.POST['Dept_name']
        dtn = request.POST['Dept_type']
        dadd = request.POST['Dept_address']
        try:
            Department.objects.create(dept_name = dn,type= dtn,address_block=dadd)
        
            error="no"
        except:
            error="yes"
    print("error ",error)
    return render(request, 'home.html',{'dp_objs': dp_objs, 'error': error, 'emp_objs':emp_objs})


def view_employee(request, pid):

    emp_obj = Employee.objects.get(id = pid)
    return render(request, 'view_employee.html',{'emp_obj':emp_obj})
    

def edit_employee(request, pid):
    print("edit employee")
    error=""
    emp_obj = get_object_or_404(Employee, id=pid)
    dp_objs = Department.objects.all()

    if request.method == 'POST':
        # Update employee fields with the data from the form
        emp_obj.emp_name = request.POST.get('Employee')
        emp_obj.email = request.POST.get('Email')
        emp_obj.mobile = request.POST.get('Mobile')
        dept_name = request.POST.get('Dept_type')  # Get department name from form
        dept_obj = get_object_or_404(Department, dept_name=dept_name)  # Get department object
        emp_obj.dept_id = dept_obj  # Assign department object to employee
        emp_obj.address = request.POST.get('Address')
        emp_obj.dob = request.POST.get('DOB')
        emp_obj.doj = request.POST.get('DOJ')
        emp_obj.gender = request.POST.get('Gender')
        
        # Save the updated employee object
        try:

            emp_obj.save()
            error="no"
        except:
            error = "yes"
        print("error ", error)
        return redirect('home')  

    return render(request, 'edit_employee.html',{'emp_obj':emp_obj,'dp_objs':dp_objs})

def delete_employee(request, pid):
    try:
        emp_obj = Employee.objects.get(id=pid)
        emp_obj.delete()
        return redirect('home')  
    except Employee.DoesNotExist:
        return HttpResponse("Employee does not exist.")