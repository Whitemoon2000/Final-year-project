from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


from .models import *
from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request, 'account/Home_page.html')

def Signup(request):
	if request.user.is_authenticated:
		return render(request, 'account/Home_page.html')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return render(request, 'account/Login_page.html')
			

		context = {'form':form}
		return render(request, 'account/Signup_page.html', context)
    

def Login(request):
	if request.user.is_authenticated:
		return render(request, 'account/Home_page.html')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return render(request, 'account/Home_page.html')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'account/Login_page.html', context)

def profile(request):
    context = {
        'user' : request.user 
    }
    return render(request, 'account/Profile_page.html', context)

def Logout(request):
    logout(request)
    return render(request, 'account/Home_page.html')