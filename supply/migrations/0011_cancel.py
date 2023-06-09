# Generated by Django 4.2.1 on 2023-06-03 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0010_delete_cancel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=10)),
                ('account', models.CharField(max_length=32)),
                ('account_holder', models.CharField(max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancel_order', to='supply.order')),
            ],
        ),
    ]
