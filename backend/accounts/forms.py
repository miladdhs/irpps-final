from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False, label='ایمیل')
    phone = forms.CharField(max_length=20, required=False, label='شماره تلفن')
    first_name = forms.CharField(max_length=150, required=True, label='نام')
    last_name = forms.CharField(max_length=150, required=True, label='نام خانوادگی')
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تکرار رمز عبور'

