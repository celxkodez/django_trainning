from .forms import NewUserForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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

@login_required
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
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="registration/register.html", context={"register_form":form})
