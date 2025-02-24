from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm


class userInfoForm(forms.ModelForm):
    class Meta:
        model=userinfoModel
        fields='__all__'
        
class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

    def save(self):
        obj=super().save()
        obj.set_password(self.cleaned_data['password'])
        obj.save()
        return obj
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    
class signinform(forms.ModelForm):
    class Meta:
        model=signinModel
        fields=['username','password']

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account found with this email address.")
        return email