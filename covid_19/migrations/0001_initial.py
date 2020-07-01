# Generated by Django 3.0.7 on 2020-06-25 10:35

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='corona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('totalcases', models.CharField(max_length=100)),
                ('newcases', models.CharField(max_length=100)),
                ('totaldeathes', models.CharField(max_length=100)),
                ('newdeathes', models.CharField(max_length=100)),
                ('totalrecovered', models.CharField(max_length=100)),
                ('activecases', models.CharField(max_length=100)),
                ('criticalcases', models.CharField(max_length=100)),
            ],
        ),
    ]
