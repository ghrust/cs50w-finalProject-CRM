# Generated by Django 3.1.3 on 2020-11-26 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201124_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='customers',
            field=models.ManyToManyField(blank=True, related_name='customers', to='api.Customer', verbose_name="company's clients"),
        ),
    ]
