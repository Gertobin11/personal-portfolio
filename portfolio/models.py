from django.db import models


class Portfolio(models.Model):
    project_name = models.CharField(max_length=254)
    project_description = models.TextField(max_length=1000)
    technologies_used = models.CharField(max_length=254)
    project_image = models.ImageField()
    live_site = models.CharField(max_length=254)
    """ I had to use charfield instead of genericipaddress
        as my heroku apps were throwing errors """

    def __str__(self):
        return self.project_name
