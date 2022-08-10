from django import forms        
from django.forms import ModelForm
from django.contrib.auth.models import User
class SignupForm(ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        labels={'username':' Enter User Name','password':' Enter Password','email':'Enter Email','first_name':'Enter First Name','last_name':'Enter Last Name'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your User Name'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'})
        }
        