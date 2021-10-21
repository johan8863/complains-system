from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Entity


# Entity's CRUD #
class EntityCreate(LoginRequiredMixin, generic.CreateView):
    model = Entity
    fields = '__all__'
    template_name = 'entities/entities_create_or_update.html'


class EntityList(LoginRequiredMixin, generic.ListView):
    model = Entity
    context_object_name = 'entities'
    template_name = 'entities/entities_list.html'


class EntityDetail(LoginRequiredMixin, generic.DetailView):
    model = Entity
    context_object_name = 'entity'
    template_name = 'entities/entities_detail.html'


class EntityUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Entity
    fields = '__all__'
    template_name = 'entities/entities_create_or_update.html'


class EntityDelete(LoginRequiredMixin, generic.DeleteView):
    model = Entity
    template_name = 'entities/entities_confirm_delete.html'



# End Entity's CRUD #