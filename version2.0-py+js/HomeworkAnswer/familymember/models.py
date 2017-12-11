from django.db import models

# Create your models here.
class familymember(models.Model):
    name = models.CharField(max_length=500)
    wife = models.CharField(max_length=500)
    info = models.TextField(null=True, blank=True)
    key = models.IntegerField(default=0)
    parent = models.IntegerField(default=0)

    def __str__(self):
        return self.name