from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from .forms import Stuform,logform,deleteform



###THIS FUNCTION IS FOR TO DISPLAY OF LOGIN,REGISTER,DELETE,UPDATE OPTIONS###
def Index(request):
    return render(request, 'Index.html')



### THIS FUNCTION IS FOR SAVING THE DATA TO DATABASE###
def sign_up_form(request):
    form = Stuform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return render(request,'tq.html')
        else:
            return form.errors
    else:
        form = Stuform()
        return render(request,'Studentregistration.html', {'form': form})


### THIS FUNCTION IS FOR RETRIEVING ALL THE DATA FROM DATABASE FOR THAT PARTICULAR CLASS###
def dtls(request):
    record = Student.objects.all()
    return render(request, 'Details.html', {'data': record})



def login_form(request):
    if request.method == 'POST':
        form =logform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            pwd=form.cleaned_data['password']
            sai =Student.objects.filter(Email=email,password=pwd )
            if not sai:
                return HttpResponse('Login failed')
            else:
                return render(request, 'Details.html', {'data': sai})

    else:
        form =logform()
        return render(request,'login.html',{'form':form})



def delete_form(request):
    if request.method == 'POST':
        form =deleteform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            ram =Student.objects.get(Email=email)
            if not ram:
                return HttpResponse('Record not found')
            else:
                ram.delete()
                return HttpResponse('Record sucessfully Deleted')
        else:
            return form.errors
    else:
        form =deleteform()
        return render(request,'login.html',{'form':form})



def home(request):
    return render(request,'Index.html')