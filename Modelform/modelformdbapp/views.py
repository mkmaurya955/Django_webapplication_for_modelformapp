from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Reg
from .forms import LoginForm
from .forms import RegForm
def home(request):
    return render(request,'home.html')
def reg(request):
    if(request.method=='POST'):
        form=RegForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('Registration successfully')
        else:
            print(form.errors)
            return HttpResponse('Errors occurred')
    else:
        form=RegForm()
        return render(request,'reg.html',{'form':form})
def Login(request):
    if(request.method=='POST'):
        MyLoginForm=LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un=MyLoginForm.cleaned_data['user']
            pw=MyLoginForm.cleaned_data['pwd']
            dbuser=Reg.objects.filter(user=un,pwd=pw)
            if not dbuser:
                return HttpResponse('Login failed')
            else:
                return HttpResponse('Login Successful')
    else:
        MyLoginForm=LoginForm()
        return render(request,'login.html',{'MyLoginForm':MyLoginForm})

