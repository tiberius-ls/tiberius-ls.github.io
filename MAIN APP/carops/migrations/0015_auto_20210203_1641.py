# Generated by Django 3.1.5 on 2021-02-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carops', '0014_auto_20210201_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='missingcar',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
