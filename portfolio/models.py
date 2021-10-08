from django.db import models


class Portfolio(models.Model):
    project_name = models.CharField(max_length=254)
    project_intro = models.CharField(max_length=254,
                                     default='This is a project \
                                     completed by Ger Tobin')
    project_description = models.TextField(max_length=1000)
    technologies_used = models.CharField(max_length=254)
    project_image = models.ImageField()
    git_hub_repo = models.CharField(max_length=254,
                                    default='https://github.com/Gertobin112')
    live_site = models.CharField(max_length=254)
    """ I had to use charfield instead of genericipaddress
        as my heroku apps were throwing errors """
    project_date = models.CharField(max_length=25)

    def __str__(self):
        return self.project_name
