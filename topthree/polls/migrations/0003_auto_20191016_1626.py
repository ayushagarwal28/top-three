# Generated by Django 2.0.2 on 2019-10-16 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20191016_1621'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Polls',
            new_name='Poll',
        ),
    ]
