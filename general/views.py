from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.views import logout_then_login
from django.urls import reverse_lazy


class Welcome(LoginRequiredMixin, generic.TemplateView):
    login_url = reverse_lazy('login')
    # template_name='general/welcome.html' to be used in the future
    template_name='complains/complains_list.html'


def logout(request):
    return logout_then_login(request, reverse_lazy('login'))