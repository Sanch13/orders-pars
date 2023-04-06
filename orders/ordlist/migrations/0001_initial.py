# Generated by Django 4.2 on 2023-04-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataIcetrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250, unique=True)),
                ('deadline', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
