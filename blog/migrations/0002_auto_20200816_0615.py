# Generated by Django 3.0.5 on 2020-08-16 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]