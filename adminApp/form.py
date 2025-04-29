from django.contrib.auth.models import User
from django import forms

class RegisterAdmin(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email')
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Password does not match')
            return cd['password2']

# login type form ==========================
class loginTypeForm(forms.Form):
    LOGIN_TYPE_CHOICES = [
        ('adminlogin', 'Admin Login'),
        ('user', 'User Login'),
    ]
    login_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=LOGIN_TYPE_CHOICES,
    )