from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView

from users.forms import ProfileUserForm, RegisterUserForm, LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


class RegistrationView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
