# Generated by Django 3.1.7 on 2021-04-27 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0003_auto_20210428_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='trains',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trains.trains'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trains.users'),
        ),
    ]
