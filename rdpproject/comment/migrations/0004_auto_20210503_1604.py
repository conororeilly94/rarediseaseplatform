# Generated by Django 3.1.4 on 2021-05-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cm',
            field=models.TextField(null=True),
        ),
    ]