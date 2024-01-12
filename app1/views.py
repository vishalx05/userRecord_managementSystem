from django.shortcuts import render,HttpResponse,redirect
from .models import Student
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['email']
        city=request.POST['city']
        contact=request.POST['contact']
        obj=Student(name=name,email=email,city=city,contact=contact,)
        obj.save()
        return redirect('records')

    else:
        pass
    return render(request,'index.html')


def records(request):
    records=Student.objects.all()
    context={
        'records':records
    }
    return render(request,'records.html',context)


def delete(request,id):

    if request.method=="POST":

        obj=Student.objects.get(id=id)
        obj.delete()
        return redirect('records')

    return render(request,'records.html')


def edit(request,id):
    data= Student.objects.get(id=id)
    context={
        'data':data
    }
    return render(request,'edit.html',context)

def update(request, id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        contact = request.POST['contact']

        updatedRecord = Student.objects.get(id=id)
        updatedRecord.name = name
        updatedRecord.email = email
        updatedRecord.city = city
        updatedRecord.contact = contact
        updatedRecord.save()

        return redirect('records')

    return render(request, "edit.html")
