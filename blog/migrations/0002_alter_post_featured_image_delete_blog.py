# Generated by Django 5.0 on 2024-01-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
