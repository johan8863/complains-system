from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Complain


# Complain's CRUD #
class ComplainCreate(LoginRequiredMixin, generic.CreateView):
    model = Complain
    fields = '__all__'
    template_name = 'complains/complains_create_or_update.html'


class ComplainList(LoginRequiredMixin, generic.ListView):
    model = Complain
    context_object_name = 'complains'
    template_name = 'complains/complains_list.html'


class ComplainDetail(LoginRequiredMixin, generic.DetailView):
    model = Complain
    context_object_name = 'complain'
    template_name = 'complains/complains_detail.html'


class ComplainUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Complain
    fields = '__all__'
    template_name = 'complains/complains_create_or_update.html'


class ComplainDelete(LoginRequiredMixin, generic.DeleteView):
    model = Complain
    template_name = 'complains/complains_confirm_delete.html'



# End Complain's CRUD #