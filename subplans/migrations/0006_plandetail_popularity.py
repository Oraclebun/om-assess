# Generated by Django 2.2.16 on 2020-09-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subplans', '0005_auto_20200903_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='plandetail',
            name='popularity',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
