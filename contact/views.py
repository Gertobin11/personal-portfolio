from django.shortcuts import render
from .forms import ContactForm1


def contact(request):
    ''' A view to return the contact page '''
    contact_form1 = ContactForm1
    template = 'contact/contact.html'
    context = {
        'contact_form1': contact_form1
    }

    return render(request, template, context)
