from enum import Enum

from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120, unique=True)
    details = models.TextField(max_length=4000)

    def __str__(self):
        return self.name


class Player(models.Model):
    striker = 'Striker'
    defender = 'Defender'
    halfdefender = 'HalfDefender'
    goalkeeper = 'Goalkeeper'
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    number = models.IntegerField()
    position_in_field = models.CharField(
        max_length=120, choices=(
            (goalkeeper, 'GoalKeeper'),
            (defender, 'Defender'),
            (halfdefender, 'HalfDefender'),
            (striker, 'Striker')
        )
    )
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.name, self.team)


class GameScore(models.Model):
    first_team_relation = models.ForeignKey(Team, related_name='first_team', on_delete=models.CASCADE, null=True)
    second_team_relation = models.ForeignKey(Team, related_name='second_team', on_delete=models.CASCADE, null=True)
    first_team_score = models.IntegerField(default=0)
    second_team_score = models.IntegerField(default=0)
    game_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} - {} {}'.format(self.first_team_relation.name, self.first_team_score, self.second_team_relation.name, self.second_team_score)