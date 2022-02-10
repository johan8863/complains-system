from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Promoter


# Promoter's CRUD #
class PromoterCreate(LoginRequiredMixin, generic.CreateView):
    model = Promoter
    fields = '__all__'
    template_name = 'promoters/promoters_create_or_update.html'


class PromoterList(LoginRequiredMixin, generic.ListView):
    model = Promoter
    context_object_name = 'promoters'
    template_name = 'promoters/promoters_list.html'


class PromoterDetail(LoginRequiredMixin, generic.DetailView):
    model = Promoter
    context_object_name = 'promoter'
    template_name = 'promoters/promoters_detail.html'


class PromoterUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Promoter
    fields = '__all__'
    template_name = 'promoters/promoters_create_or_update.html'


class PromoterDelete(LoginRequiredMixin, generic.DeleteView):
    model = Promoter
    template_name = 'promoters/promoters_confirm_delete.html'
    success_url = reverse_lazy('promoters_list')



# End Promoter's CRUD #