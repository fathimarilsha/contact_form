from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","phone","email"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"first name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"last name"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),
            "password":forms.TextInput(attrs={"class":"form-control","placeholder":"password"}),
            "phone":forms.IntegerField(attrs={"class":"form-control","placeholder":"phone number"}),
            "email":forms.EmailField(attrs={"class":"form-control","placeholder":"email"})
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}),
        }