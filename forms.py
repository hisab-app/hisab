from django import forms

class LoginForm(forms.Form):
    email=forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-control','required':False}))
    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form-control','required':False}))
        