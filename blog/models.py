from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=80)
    date = models.DateField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title, self.date