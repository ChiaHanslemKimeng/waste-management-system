from django.shortcuts import render
from django.shortcuts import render, redirect
from adminApp.form import RegisterAdmin, loginTypeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
# registration ======================================================================>>>>
def Register(request):
    if request.method == "POST":
        regForm = RegisterAdmin(request.POST)
        if regForm.is_valid():
            new_user = regForm.save(commit=False)
            new_user.set_password(regForm.cleaned_data.get('password'))
            new_user.save()
            return redirect('adminApp:login')
    else:
        form = RegisterAdmin()
        return render(request, 'templates/register.html', {'form': form})
    
# def logoutview(request):
#     logout(request)
#     return redirect('userRegister:login')
# login view ==============================================================================
def login_type_view(request):
    if request.method == 'POST':
        forms = loginTypeForm(request.POST)
        if forms.is_valid():
            login_type = forms.cleaned_data['login_type']
            if login_type == 'adminlogin':
                return redirect('adminApp:login')
            else:
                return redirect('adminApp:adminpanel')
    else:
        forms = loginTypeForm()
        return render(request, 'apptemplates/logintype.html', {'forms': forms})

def admin_login_view(request):
    return redirect('adminApp:adminpanel')
