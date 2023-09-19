from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label="User Name")
    file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # password = forms.CharField()
    
class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(),min_length=5)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    conf_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        val_password = self.cleaned_data['password']
        val_conf_password = self.cleaned_data['conf_password']
        if val_password != val_conf_password:
            raise forms.ValidationError("Password doesn't match")