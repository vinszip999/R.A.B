# Generated by Django 2.2.23 on 2021-06-29 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rab', '0015_auto_20210629_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='images',
            new_name='image',
        ),
    ]
