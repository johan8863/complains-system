from complains.models import Complain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login
from django.urls import reverse_lazy
from django.views import generic


class Welcome(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    model = Complain
    context_object_name = 'complains'
    template_name='complains/complains_list.html'
    # template_name='general/welcome.html' might be used in the future


def logout(request):
    return logout_then_login(request, reverse_lazy('login'))