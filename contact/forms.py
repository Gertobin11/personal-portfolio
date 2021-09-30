from django import forms
from .models import ContactForm


class ContactForm1(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('fullname', 'email', 'phone_number',
                  'comments')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fullname': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'comments': 'Comments',
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields['fullname'].widget.attrs['autofocus'] = True
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
