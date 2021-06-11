from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Http Logger
from .utilities.dumper import dd
# from django.views.generic import TemplateView

# class HomeView(TemplateView):
#     template_name='polls/pages/index.html'
#
#     def get(self, request, *args, **kwargs):
#         context = locals()
#         context['page_title'] = 'Polls App'
#         context['range'] = range(8)
#
#         return render(request, self.template_name, context)

@login_required(login_url='/login')
def index(request):
    page_title = 'Polls App'
    return render(request, 'polls/pages/index.html', { "page_title": page_title, 'range' : range(8) })

def contact(request):
    page_title = 'Polls App'
    return render(request, 'polls/pages/contact.html', { "page_title": page_title })

def about(request):
    page_title = 'Polls App'
    return render(request, 'polls/pages/about.html', { "page_title": page_title })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
# 		return dd(form.is_valid())
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
# 			return dd(True)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})