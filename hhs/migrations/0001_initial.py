# Generated by Django 3.1.3 on 2020-11-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('troom', models.CharField(max_length=100)),
                ('tbal', models.CharField(max_length=100)),
                ('tchimney', models.CharField(max_length=100)),
                ('tsofa', models.CharField(max_length=100)),
                ('tcarpet', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('ph1', models.CharField(max_length=100)),
                ('ph2', models.CharField(max_length=100)),
            ],
        ),
    ]