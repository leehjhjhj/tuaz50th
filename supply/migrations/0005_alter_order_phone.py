# Generated by Django 4.2.1 on 2023-06-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0004_rename_username_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
