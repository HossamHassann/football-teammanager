# Generated by Django 2.2 on 2019-04-14 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_gamesocre_player'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameSocre',
            new_name='GameScore',
        ),
        migrations.RenameField(
            model_name='gamescore',
            old_name='first_team_socre',
            new_name='first_team_score',
        ),
    ]