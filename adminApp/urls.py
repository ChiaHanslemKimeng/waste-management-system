from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from adminApp import views

app_name = "adminApp"

urlpatterns = [
    # path("", LoginView.as_view(template_name='apptemplates/logintype.html'), name="login_type"),
    path("registrationpage/", views.Register, name="Register"),
    # path('admin_login/', views.admin_login_view, name='admin_login'),
    path('admin_panel/', views.admin_login_view, name='adminpanel'),
    path('login_type/', views.login_type_view, name='login_type'),
    # path("logout/", views.logoutview, name="logout"),
]
