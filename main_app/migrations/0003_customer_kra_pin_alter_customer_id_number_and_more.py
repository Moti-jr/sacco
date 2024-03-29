# Generated by Django 5.0 on 2023-12-07 09:45

import main_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_customer_id_photo_back_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='kra_pin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id_number',
            field=models.CharField(help_text='Enter your Kenyan national ID number', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=main_app.models.generate_unique_name),
        ),
    ]
