from django.shortcuts import render, redirect, reverse
from .forms import ContactForm1
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail


def send_confirmation_email(form_data):
    # Send the user a confirmation email upon completing the contact form
    form_data = form_data
    cust_email = form_data['email']
    subject = render_to_string(
        'contact/confirmation_emails/confirmation_email_subject.txt',
        {'form_data': form_data}
    )
    body = render_to_string(
        'contact/confirmation_emails/confirmation_email_body.txt',
        {'form_data': form_data, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


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
            print(form_data)

            messages.success(request, 'Thanks for getting in touch, \
                             I will get back to you as fast as I can')
            # Send the email with the completed form data
            send_confirmation_email(form_data)
            return redirect(reverse('home'))
    else:
        contact_form1 = ContactForm1
        template = 'contact/contact.html'
        context = {
            'contact_form1': contact_form1
        }

        return render(request, template, context)
