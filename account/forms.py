from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'is_ITManager',
            'is_sectorIT',
            'sector'
        ]

    #
    # def save(self, commit=True):
    #     user = super(RegisterUser, self).save(commit=False)
    #     user.firstName = self.cleaned_data['firstName']
    #     user.lastName = self.cleaned_data['lastName']
    #     user.email = self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user