# Generated by Django 3.2.7 on 2021-10-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_description',
            field=models.TextField(max_length=1000),
        ),
    ]