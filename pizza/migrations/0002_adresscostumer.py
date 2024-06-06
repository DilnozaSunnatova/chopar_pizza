# Generated by Django 5.0.6 on 2024-06-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdressCostumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=200)),
                ('kvartira', models.CharField(max_length=150)),
                ('podez', models.CharField(max_length=150)),
                ('enter_code', models.IntegerField()),
                ('dom', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
