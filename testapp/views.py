from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from staff_view.views import StaffView


User = get_user_model()


class AddUserForm(forms.ModelForm):

    class Meta:
        fields = ('username', 'email')
        model = User


class QuickAddUserView(StaffView):

    confirm_message = _("Add user")

    form_class = AddUserForm

    title = _("Add user")

    def form_valid(self, username, email):
        user = User.objects.create_user(username, email)
        return redirect(reverse('admin:auth_user_change', args=[user.pk]))
