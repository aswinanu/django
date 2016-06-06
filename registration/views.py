

from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from forms import UserRegistrationForm
from forms import ChocolateAddForm
class Home(TemplateView):
    template_name='index.html'

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

