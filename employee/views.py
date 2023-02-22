from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
# from templates import show,edit,index

# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
def show(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees})
def edit(request,id):
    employees = Employee.objects.all()
    return render(request,'edit.html',{'employees':employees})
def update(request,id):
    employees= Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,instance = employees)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'employee':employees})
     
def destroy(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
    

