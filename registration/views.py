

from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from forms import UserRegistrationForm
from forms import ChocolateAddForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from models import Chocolate


class Home(ListView):
    template_name='index.html'


    def get_queryset(self):
        return Chocolate.objects.all()


# Create your views here.
class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

class AddChocolateView(FormView):
    template_name = "add_chocolate.html"
    form_class = ChocolateAddForm
    success_url = '/registration/chocolates/success'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

class ListChocolateView(ListView):
    template_name='list_chocolate.html'

    def get_queryset(self):
        return Chocolate.objects.all()

class ChocolateDetailsView(DetailView):
    template_name = 'chocolate_detail.html'

    def get_object(self, queryset=None):
        choco_id = self.kwargs['choco_id']
        obj = Chocolate.objects.get(id=choco_id)
        if obj:
            return obj
        else:
            raise Http404("No details Found.")
