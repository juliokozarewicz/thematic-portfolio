# Generated by Django 4.1.5 on 2023-04-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='slug',
            field=models.CharField(default='---', max_length=250),
        ),
    ]
