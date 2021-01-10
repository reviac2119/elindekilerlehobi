from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, label="Kullanıcı Adı")
    password = forms.CharField(max_length=25, label="Şifre", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adını veya şifreyi yanlış girdiniz!')
        return super(LoginForm, self).clean()


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=25, label="Kullanıcı Adı")
    password = forms.CharField(max_length=25, label="Şifre", widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=25, label="Şifre Tekrar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            're_password',
        ]

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password and re_password and password != re_password:
            raise forms.ValidationError('Parolalar eşleşmiyor! Lütfen tekrar deneyin.')
        return re_password