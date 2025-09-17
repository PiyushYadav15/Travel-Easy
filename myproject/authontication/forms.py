from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

#  register form

class RegisterForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput) # inbuild password
    confirm_password=forms.CharField(label='Confirm Password',widget=forms.PasswordInput) # inbuild password

    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
    def clean(self):
        cleaned_data= super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password!=confirm_password:
            raise forms.ValidationError('password do not match')
        return cleaned_data

class loginform(forms.Form):
    username=forms.CharField(label='username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']



class Password_change_form(PasswordChangeForm):
    old_password=forms.CharField(label='Current Password',widget=forms.PasswordInput)
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput)
    confirm_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)


