# Generated by Django 2.1.7 on 2019-05-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0043_auto_20190516_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='deleted',
            field=models.BooleanField(default=False, help_text='Provider has been deleted'),
        ),
    ]
