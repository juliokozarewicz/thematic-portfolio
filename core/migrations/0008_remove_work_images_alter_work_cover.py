# Generated by Django 4.1.5 on 2023-04-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_work_image_work_cover_work_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='images',
        ),
        migrations.AlterField(
            model_name='work',
            name='cover',
            field=models.ImageField(default='', upload_to='works/'),
        ),
    ]
