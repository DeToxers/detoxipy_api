# Generated by Django 2.1.2 on 2018-10-17 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('message', models.CharField(max_length=48)),
                ('total', models.IntegerField()),
                ('time_updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('message', models.CharField(max_length=48)),
                ('total', models.IntegerField()),
                ('weight', models.FloatField()),
                ('time_updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SessionCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_five', models.TextField()),
                ('room_id', models.IntegerField()),
            ],
        ),
    ]
