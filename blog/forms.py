from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='ник', required=True, widget=forms.TextInput(attrs ={'class': "form-control mb-20"}))
    email = forms.CharField(label='E-mail', required=True, widget=forms.TextInput(attrs ={'class': "form-control mb-20"}))
    password1 = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(attrs ={'class': "form-control mb-20"}))
    password2 = forms.CharField(label='Повторите пароль', required=True, widget=forms.PasswordInput(attrs ={'class': "form-control mb-20"}))
    firs_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs ={'class': "form-control mb-20"}))
    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(attrs ={'class': "form-control mb-20"}))

    class Meta:
        model = User
        fields = ('username', "email", 'first_name', 'last_name', 'password1', 'password2')

    def save(self,commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user