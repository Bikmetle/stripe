# Generated by Django 4.1.1 on 2022-09-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripeApp', '0002_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
