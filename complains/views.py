from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .forms import ComplainForm
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
    form_class = ComplainForm
    # fields = '__all__'
    template_name = 'complains/complains_create_or_update.html'


class ComplainDelete(LoginRequiredMixin, generic.DeleteView):
    model = Complain
    template_name = 'complains/complains_confirm_delete.html'
    success_url = reverse_lazy('complains_list')



# End Complain's CRUD #