from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Person

# Person's CRUD #
class PersonCreate(LoginRequiredMixin, generic.CreateView):
    model = Person
    fields = ['name', 'last_name', 'sex']
    template_name = 'persons/persons_create_or_update.html'


class PersonList(LoginRequiredMixin, generic.ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'persons/persons_list.html'


class PersonDetail(LoginRequiredMixin, generic.DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'persons/persons_detail.html'


class PersonUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Person
    fields = ['name', 'last_name', 'sex']
    template_name = 'persons/persons_create_or_update.html'


class PersonDelete(LoginRequiredMixin, generic.DeleteView):
    model = Person
    template_name = 'persons/persons_confirm_delete.html'
    success_url = reverse_lazy('persons_list')

# End Person's CRUD #