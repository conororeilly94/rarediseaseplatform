# Generated by Django 3.1.4 on 2021-01-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210114_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='link',
        ),
        migrations.RemoveField(
            model_name='main',
            name='tel',
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
