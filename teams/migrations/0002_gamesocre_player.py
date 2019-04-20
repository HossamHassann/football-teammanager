# Generated by Django 2.2 on 2019-04-14 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSocre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team', models.CharField(max_length=120)),
                ('second_team', models.CharField(max_length=120)),
                ('first_team_socre', models.IntegerField(default=0)),
                ('second_team_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('number', models.IntegerField()),
                ('position_in_field', models.CharField(choices=[('1', 'goalkeeper'), ('2', 'defender'), ('3', 'halfdefender'), ('4', 'striker')], max_length=120)),
                ('i_captain', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
    ]