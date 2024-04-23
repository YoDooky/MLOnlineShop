from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class UserLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Please sign in before checkout")
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
