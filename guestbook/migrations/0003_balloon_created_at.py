# Generated by Django 4.2.1 on 2023-08-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_alter_balloon_body_alter_balloon_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='balloon',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
