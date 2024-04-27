from django.shortcuts import render

from allauth.account.views import LoginView, LogoutView


class AccountLoginView(LoginView):
    template_name = "custom_login.html"


