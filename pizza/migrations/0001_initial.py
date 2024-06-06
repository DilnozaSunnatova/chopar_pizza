# Generated by Django 5.0.6 on 2024-06-06 10:03

import django.db.models.deletion
import django.utils.timezone
import pizza.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_up', models.DateField()),
                ('updated_up', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='basket')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number', models.IntegerField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('link', models.URLField()),
                ('description', models.TextField()),
                ('order_numbere', models.CharField(max_length=10)),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='discount')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='extra')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=20, null=True, unique=True, validators=[pizza.models.UnicodePhoneValidator()])),
                ('status', models.CharField(choices=[('new', 'Yangi'), ('approved', 'Tasdiqlangan')], default='new', max_length=50)),
                ('code', models.CharField(max_length=4, null=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=200)),
                ('birth_date', models.DateField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', pizza.models.PhoneManager()),
            ],
        ),
        migrations.CreateModel(
            name='UsertLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
                ('apartment', models.CharField(max_length=100)),
                ('podyezd', models.IntegerField()),
                ('code', models.IntegerField()),
                ('adress_name', models.CharField(max_length=200)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.region')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pizza.basemodel')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='product1')),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.menu')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza.productsize')),
            ],
            bases=('pizza.basemodel',),
        ),
    ]
