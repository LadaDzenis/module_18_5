from django import forms
from django.core.exceptions import ValidationError
#from .views import users

class UserRegister(forms.Form):
    username = forms.CharField(max_length=100, label='Введите логин:')
    password = forms.CharField(widget=forms.PasswordInput, min_length=8,
                               label='Введите пароль:')
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8,
                                      label='Повторите пароль:')
    age = forms.IntegerField(min_value=1, max_value=100, label='Введите свой возраст:')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if username in users:
    #         raise forms.ValidationError('Пользователь уже существует')
    #     return username
    #
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if password != self.repeat_password:
    #         raise forms.ValidationError('Пароли не совпадают')
    #     return password
    #
    # def clean_age(self):
    #     age = self.cleaned_data.get('age')
    #     if age < self.age:
    #         raise forms.ValidationError('Вы должны быть старше 18')
    #     return age