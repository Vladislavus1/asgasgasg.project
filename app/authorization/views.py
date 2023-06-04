from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
from .forms import SignupForm
from django.contrib import messages

class SignupView(CreateView):
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.warning(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context