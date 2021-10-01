from django.shortcuts import render, redirect, reverse
from .forms import ContactForm1
from django.contrib import messages


def contact(request):
    ''' A view to return the contact page '''
    if request.method == 'POST':
        form_data = {
            'fullname': request.POST['fullname'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'comments': request.POST['comments'],
        }

        contact_form = ContactForm1(form_data)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thanks for getting in touch, \
                             I will get back to you as fast as I can')
            return redirect(reverse('home'))
    else:
        contact_form1 = ContactForm1
        template = 'contact/contact.html'
        context = {
            'contact_form1': contact_form1
        }

        return render(request, template, context)
