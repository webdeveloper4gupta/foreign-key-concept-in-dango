from django.shortcuts import render
from .models import employee
from .forms import employeeform
# Create your views here.

def home(request):
    form=employeeform()
    if request.method=="POST":
        n1=request.POST.get('name')
        n2=request.POST.get('company')
        n3=request.POST.get('ctc')
        n4=request.POST.get('dept_id')
        form= employeeform(request.POST)
        if form.is_valid():
            employee(name=n1,company=n2,ctc=n3,dept_id_id=n4).save()
    
    return render(request,"home.html",{'forms':form})



    