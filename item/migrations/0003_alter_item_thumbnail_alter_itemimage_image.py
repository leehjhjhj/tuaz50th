# Generated by Django 4.2.1 on 2023-05-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_remove_itemimage_thumbnail_item_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='item_thumbnails/'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(upload_to='item_images/'),
        ),
    ]
