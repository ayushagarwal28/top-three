# Generated by Django 2.1.5 on 2019-10-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20191023_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateField(),
        ),
    ]