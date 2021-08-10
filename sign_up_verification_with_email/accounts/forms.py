from django import forms
from .models import Users


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=15)

    class Meta:
        model = Users
        fields = ('email', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise ValueError("Password must be at least 8 charecters")
        return password

    def save(self):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
