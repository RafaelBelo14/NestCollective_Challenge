# Generated by Django 3.2.3 on 2021-05-31 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tascasApp', '0002_remove_tasca_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasca',
            name='rating',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
    ]
