# Generated by Django 3.2.3 on 2021-06-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tascasApp', '0005_alter_tasca_tascapicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasca',
            name='tascaPicture',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]