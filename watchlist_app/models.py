from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Meta:
    verbose_name = "Movie"
    verbose_name_plural = "Movies"
