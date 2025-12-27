from django.db import models

# Create your models here.
class users(models.Model):

    role_choices = [
        ('user', 'user'),
        ('team-member', 'Team-Member'),
        ('team-lead', 'Team-Lead'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=role_choices, default='user')

    def __str__(self):
        return self.username

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(users, related_name='teams')
    team_lead = models.ForeignKey(users, on_delete=models.CASCADE, related_name='led_teams')

    def __str__(self):
        return self.name

