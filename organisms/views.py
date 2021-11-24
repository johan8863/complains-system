from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Organism


# Organism's CRUD #
class OrganismCreate(LoginRequiredMixin, generic.CreateView):
    model = Organism
    fields = '__all__'
    template_name = 'organisms/organisms_create_or_update.html'


class OrganismList(LoginRequiredMixin, generic.ListView):
    model = Organism
    context_object_name = 'organisms'
    template_name = 'organisms/organisms_list.html'


class OrganismDetail(LoginRequiredMixin, generic.DetailView):
    model = Organism
    context_object_name = 'organism'
    template_name = 'organisms/organisms_detail.html'


class OrganismUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Organism
    fields = '__all__'
    template_name = 'organisms/organisms_create_or_update.html'


class OrganismDelete(LoginRequiredMixin, generic.DeleteView):
    model = Organism
    template_name = 'organisms/organisms_confirm_delete.html'
    success_url = reverse_lazy('organisms_list')



# End Organism's CRUD #