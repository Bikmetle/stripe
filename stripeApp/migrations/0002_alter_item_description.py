# Generated by Django 4.1.1 on 2022-09-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
