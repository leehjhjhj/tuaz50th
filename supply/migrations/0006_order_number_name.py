# Generated by Django 4.2.1 on 2023-06-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0005_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number_name',
            field=models.CharField(default='임시', max_length=10),
        ),
    ]