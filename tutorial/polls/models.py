from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
