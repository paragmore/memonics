# Generated by Django 3.0.5 on 2020-05-03 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.Chapter'),
        ),
    ]
