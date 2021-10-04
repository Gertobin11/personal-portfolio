# Generated by Django 3.2.7 on 2021-10-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_portfolio_live_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='git_hub_repo',
            field=models.CharField(default='https://github.com/Gertobin112', max_length=254),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='project_intro',
            field=models.CharField(default='This is a project                                      completed by Ger Tobin', max_length=254),
        ),
    ]
