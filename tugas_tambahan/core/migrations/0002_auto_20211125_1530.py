# Generated by Django 3.2.9 on 2021-11-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
