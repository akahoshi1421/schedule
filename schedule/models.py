from django.db import models

# Create your models here.
class task(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    time = models.IntegerField()
    content = models.CharField(max_length=200)
    conect = models.IntegerField()

    def __str__(self):
        return self.content
    