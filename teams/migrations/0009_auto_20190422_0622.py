# Generated by Django 2.2 on 2019-04-22 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20190422_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
