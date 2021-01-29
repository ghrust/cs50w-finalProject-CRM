# Generated by Django 3.1.3 on 2020-11-24 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name="customer's email address")),
                ('phone_number', models.CharField(max_length=20, verbose_name="customer's phone number")),
                ('address', models.CharField(blank=True, max_length=200, verbose_name="customer's address")),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2020, 11, 24, 14, 2, 10, 475790), verbose_name='date joined')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='customers',
            field=models.ManyToManyField(related_name='customers', to='api.Customer', verbose_name="company's client"),
        ),
    ]