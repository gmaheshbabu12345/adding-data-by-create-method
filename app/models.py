from django.db import models

# Create your models here.
class Ipl(models.Model):
    teamno=models.IntegerField(primary_key=True)
    team=models.CharField(max_length=100)
    def __str__(self):
        return self.team
class teams(models.Model):
   teamno=models.ForeignKey(Ipl('teamno'),on_delete=models.CASCADE)
   purseleft=models.IntegerField()
   def __str__(self):
      return self.teamno