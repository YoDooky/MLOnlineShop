from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from django.contrib import messages
from social_django.utils import psa

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import ProfileUserForm, RegisterUserForm, LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        # save last session_key before success login
        self.request.session['last_session_key'] = self.request.session.session_key
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Login Successfully")
        # add unauth user cart to current successfully login user cart (via session_key)
        last_session_key = self.request.session['last_session_key']
        if last_session_key:
            Cart.objects.filter(session_key=last_session_key).update(user=self.request.user)
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
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_orders'] = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('product'),
            ))
        return context

    def get_success_url(self):
        messages.success(self.request, "Profile has been changed")
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def users_cart(req):
    return render(req, 'users/users_cart.html')


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy("users:profile")  # del

    def get_success_url(self):
        messages.success(self.request, "Password has been changed")
        return reverse_lazy('users:profile')


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy("users:password_reset_done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'

    def get_success_url(self):
        messages.success(self.request, "You have been successfully reset your password. Please login")
        return reverse_lazy('users:profile')
