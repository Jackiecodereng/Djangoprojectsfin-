# Generated by Django 5.1.3 on 2024-11-14 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customers',
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco.customer')),
            ],
            options={
                'db_table': 'deposits',
            },
        ),
    ]
