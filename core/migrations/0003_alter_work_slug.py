# Generated by Django 4.1.5 on 2023-04-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_work_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='slug',
            field=models.CharField(default='', max_length=250),
        ),
    ]
