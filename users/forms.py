from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):

    username = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()

        if not User.objects.filter(username=username).exists():
            return username

        raise forms.ValidationError('{0} exists, use other username'.format(username))

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Passwords don\'t match')
