# Generated by Django 2.2 on 2019-04-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20190415_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position_in_field',
            field=models.CharField(choices=[('goal', 'Goalkeeper'), ('def', 'Defender'), ('half', 'Halfdefender'), ('st', 'Striker')], max_length=120),
        ),
    ]
