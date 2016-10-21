from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import MoneyUser


class MoneyUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(MoneyUserCreationForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    class Meta:
        model = MoneyUser
        fields = ("email",)


class MoneyUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(MoneyUserChangeForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    class Meta:
        model = MoneyUser
        exclude = ()
