# Generated by Django 2.2.23 on 2021-06-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rab', '0016_auto_20210629_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
