from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Users
class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username','email','password']
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username','email','password','phone','aadharid']

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    phone = forms.CharField(max_length=10,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': '10 digit Phone Number',
                                                                  'class': 'form-control',
                                                                  'data-toggle': '10 digit Phone number',
                                                                  'id': 'phone',}))
    aadharid = forms.CharField(max_length=4,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Last 4 digits of Aadhaar ID',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'Last 4 digit of Aadhaar ID',
                                                                  'id': 'aadharid',}))
    address = forms.CharField(max_length=150,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Your permanent address',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'Address',
                                                                  'id': 'address',}))
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2','phone','aadharid','address']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

    class Meta:
        model = Users
        fields = ['username', 'password']


class NumberForm(forms.Form):
    number_book = forms.IntegerField(max_value=100)