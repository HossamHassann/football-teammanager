# Generated by Django 2.2 on 2019-04-14 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20190415_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position_in_field',
            field=models.CharField(choices=[('goalkeeper', '1'), ('defender', '2'), ('halfdefender', '3'), ('striker', '4')], max_length=120),
        ),
    ]
