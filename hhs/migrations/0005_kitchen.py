# Generated by Django 3.1.3 on 2020-11-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhs', '0004_sofa'),
    ]

    operations = [
        migrations.CreateModel(
            name='kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('tcupboard', models.CharField(max_length=100)),
                ('tchimney', models.CharField(max_length=100)),
                ('tfridge', models.CharField(max_length=100)),
                ('tro', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('ph1', models.CharField(max_length=100)),
                ('ph2', models.CharField(max_length=100)),
                ('otser', models.TextField(default='')),
            ],
        ),
    ]
