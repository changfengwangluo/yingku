from django import forms
from captcha.fields import CaptchaField

class UserRegisterForm(forms.Form):
    username=forms.CharField(required=True,min_length=11,max_length=11)
    password=forms.CharField(required=True,min_length=6,max_length=11)
    captcha=CaptchaField()




