# Generated by Django 3.0.7 on 2020-06-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200619_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnet',
            name='content',
            field=models.TextField(default='...'),
            preserve_default=False,
        ),
    ]
