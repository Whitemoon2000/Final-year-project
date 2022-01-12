from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'account/Home_page.html')

def Signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Login')
    else :
        form = UserCreationForm()
    return render(request, 'account/Signup_page.html',{'form':form})
    

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/Login_page.html',{'form':form})

def profile(request):
    context = {
        'user' : request.user 
    }
    return render(request, 'account/Profile_page.html', context)