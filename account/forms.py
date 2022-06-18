from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import CallbackRequest


class CallbackRequestForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "name",
            "name": 'name',
            "class": "form-control",
            "type": "text",
            "required": "",
            "placeholder": "John Juma",
        }
    ))

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "phone",
            "name": "phone",
            "class": "form-control",
            "type": "tel",
            "required": "",
            "placeholder": "712345678",
        }
    ))

    id_number = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "id-number",
            "name": "id-number",
            "class": "form-control",
            "type": "text",
            "required": "",
            "placeholder": "37174841",
        }
    ))

    class Meta:
        model = CallbackRequest
        fields = ('name', 'phone', 'id_number')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "border rounded-pill border-success form-control",
            "type": "text",
            "autocomplete": "off",
            "required": "",
            "placeholder": "Username or Email"
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "border rounded-pill border-success form-control",
            "id": "exampleInputPassword",
            "type": "password",
            "required": "",
            "placeholder": "Password"
        }
    ))


attrs_class = "border rounded-pill border-success form-control"


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "border rounded-pill border-success form-control",
            "type": "text",
            "required": "",
            "placeholder": "Username..."
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            "class": attrs_class,
            "type": "email",
            "required": "",
            "placeholder": "Email...",
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            "class": attrs_class,
            "type": "password",
            "required": "",
            "placeholder": "Choose Password",
            "name": "password"
        }
    ))
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput(
        attrs={
            "class": attrs_class,
            "type": "password",
            "required": "",
            "placeholder": "Confirm Password",
            "name": "password2"
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

