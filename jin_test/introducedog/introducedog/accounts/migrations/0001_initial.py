# Generated by Django 2.1 on 2020-09-16 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=128, null=True)),
                ('user_email', models.CharField(max_length=128, null=True)),
                ('user_password', models.CharField(max_length=128, null=True)),
                ('user_profile', models.CharField(max_length=300, null=True)),
                ('match_dog', models.IntegerField(null=True)),
                ('same_dog', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
