# Generated by Django 3.2 on 2021-04-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='date',
            field=models.DateField(),
        ),
    ]
