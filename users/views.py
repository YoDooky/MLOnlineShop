from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from django.contrib import messages
from users.forms import ProfileUserForm, RegisterUserForm, LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        messages.success(self.request, "Login Successfully")
        if self.request.POST.get('next', None):
            return self.request.POST.get('next')
        return reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['get_request'] = self.request.GET.get('next')
        return context


def logout_view(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect(reverse('main:index'))


class RegistrationView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class ProfileView(LoginRequiredMixin, UpdateView):
    # raise_exception = True
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_success_url(self):
        messages.success(self.request, "Profile has been changed")
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
