# Generated by Django 3.0.5 on 2020-05-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200504_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]