from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget = forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget = forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget = forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email = forms.CharField(
#         widget = forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
# dagdag
#     user_role = forms.CharField(
#         widget = forms.Select(
#             choices= list(User.user_role_choices),
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )


#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'user_role')