# Generated by Django 3.1.5 on 2021-03-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20210223_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='product category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
