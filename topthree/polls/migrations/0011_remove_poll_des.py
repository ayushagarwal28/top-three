# Generated by Django 2.1.5 on 2019-10-27 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_poll_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='des',
        ),
    ]
