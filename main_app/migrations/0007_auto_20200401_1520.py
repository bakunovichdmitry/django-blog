# Generated by Django 2.2.6 on 2020-04-01 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_customuser_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='images',
            new_name='images',
        ),
    ]