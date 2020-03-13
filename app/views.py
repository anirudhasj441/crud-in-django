from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Employee
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"app/index.html")

def add(request):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            qua = request.POST["qua"]
            cont = request.POST["cont"]
            email = request.POST["email"]
            Employee.objects.create(name = name,qualification=qua,contact=cont,email=email)
            messages.success(request,"data add succesfullly")
        except Exception:
            pass
            messages.error(request,"NOt add")

    return render(request,'app/add.html')

def view(request):
    employees = Employee.objects.all()
    for i in employees:
        print(i.name)
    params = {
        "employees":employees,
    }
    return render(request,"app/view.html",params)

def delete(request,id):
    Employee.objects.filter(pk=id).delete()
    return redirect("/view/")
def update(request,id):
    employee = Employee.objects.get(pk=id)
    if request.method == "POST":
        # try:
            name = request.POST["name"]
            qua = request.POST["qua"]
            cont = request.POST["cont"]
            email = request.POST["email"]
            employee.name = name
            employee.qualification = qua
            employee.contact = cont
            employee.email = email
            employee.save()
            messages.success(request,"data add succesfullly")
            return redirect("/view/")
        # except Exception:
        #     messages.error(request,"NOt add")
    params = {
        "employee":employee,
    }
    return render(request,"app/update.html",params)