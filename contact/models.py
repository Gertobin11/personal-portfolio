from django.db import models


class ContactForm(models.Model):
    """ Model to store the contact information left by visitors to the site """
    fullname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    comments = models.TextField(max_length=500, null=False, blank=True)

    def __str__(self):
        return self.fullname
