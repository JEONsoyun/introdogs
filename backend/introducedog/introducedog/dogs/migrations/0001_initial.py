# Generated by Django 2.2.7 on 2020-09-22 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_id', models.CharField(max_length=20, null=True)),
                ('shelter_name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('sex', models.CharField(default='Q', max_length=10)),
                ('kind', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('neuter', models.CharField(max_length=10)),
                ('thumnail', models.CharField(max_length=300)),
                ('profile', models.CharField(max_length=300)),
                ('careAddr', models.CharField(max_length=300)),
                ('special', models.CharField(max_length=300)),
                ('find_place', models.CharField(max_length=300)),
                ('find_date', models.IntegerField()),
                ('end_date', models.IntegerField()),
            ],
        ),
    ]