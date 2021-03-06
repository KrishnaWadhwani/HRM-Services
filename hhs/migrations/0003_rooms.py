# Generated by Django 3.1.3 on 2020-11-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhs', '0002_home_otser'),
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('tfans', models.CharField(max_length=100)),
                ('talmirah', models.CharField(max_length=100)),
                ('tflooring', models.CharField(max_length=100)),
                ('tarea', models.CharField(max_length=100)),
                ('tcarpet', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('ph1', models.CharField(max_length=100)),
                ('ph2', models.CharField(max_length=100)),
                ('otser', models.TextField(default='')),
            ],
        ),
    ]
