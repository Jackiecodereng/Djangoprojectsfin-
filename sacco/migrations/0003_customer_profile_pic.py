# Generated by Django 5.1.3 on 2024-11-16 16:13

import sacco.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0002_alter_customer_table_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=sacco.models.generate_unique_name),
        ),
    ]
