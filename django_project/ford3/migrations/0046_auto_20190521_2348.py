# Generated by Django 2.1.7 on 2019-05-21 21:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0045_campusevent_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualificationevent',
            name='date_end',
            field=models.DateField(default=django.utils.timezone.now, help_text='When does this event end?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qualificationevent',
            name='date_start',
            field=models.DateField(default=django.utils.timezone.now, help_text='When does this event start?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qualificationevent',
            name='http_link',
            field=models.URLField(blank=True, help_text='A link to a web page with additional details regarding this event', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='qualificationevent',
            name='name',
            field=models.CharField(default='Default', help_text='A short identifier for the event', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='saqaqualification',
            name='field_of_study',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ford3.FieldOfStudy'),
        ),
    ]
