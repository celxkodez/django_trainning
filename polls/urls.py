from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from polls.views import HomeView
from . import views

app_name = "main"

urlpatterns = [
#   path('index', views.index, name='index'),
  path('', views.index, name="index"),
  path('contact', views.contact, name="contact"),
  path('about', views.about, name="about"),
  path('register', views.register_request, name="register"),
  path('login', views.login_request, name="login"),

#   path('other', HomeView.as_view()),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
