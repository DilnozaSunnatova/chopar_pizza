# Generated by Django 5.0.4 on 2024-06-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_branche'),
    ]

    operations = [
        migrations.AddField(
            model_name='branche',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='branche',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
