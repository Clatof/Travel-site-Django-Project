from django import forms
from django.contrib.auth.forms import AuthenticationForm

from home.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", 
                                           "placeholder": "Full Name *"}),
            "email": forms.EmailInput(attrs={"class": "form-control", 
                                             "placeholder": "Email *"}),
            "message": forms.Textarea(attrs={"class": "form-control", 
                                             "placeholder": "Message *"})
        }

