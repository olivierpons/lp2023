from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic

from recipes.forms.register import RegisterForm


class RegisterFormView(generic.FormView):
    template_name = 'register_form.html'
    form_class = RegisterForm

    # class RendezVous(models.Model):
    #     date_debut = models.DateTime(...)

    def form_valid(self, form):
        # user = self.request.user
        # rendez_vous = form.cleaned_data['rendez_vous']
        # RendezVous.objects.create(user=user, rendez_vous=...)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            User.objects.create_user(
                username=username, email=email, password=password
            )
            messages.add_message(
                self.request, messages.INFO,
                'User created successfully.'
            )
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
