# Generated by Django 3.1.5 on 2021-02-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(verbose_name="Customer's phone number"),
        ),
    ]
