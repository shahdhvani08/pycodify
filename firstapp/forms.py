from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
  class Meta:
    model = SignUp
    fields = ['full_name', 'email']

  def clean_email(self):
    email = self.cleaned_data.get('email')
    email_base, provider = email.split("@")
    domain, extension = provider.split('.')
    if not extension == "edu":
      raise forms.ValidationError("Please use a valid .EDU email address")
    return 'Thanks'

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())