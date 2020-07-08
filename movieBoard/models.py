from django.db import models

# Create your models here.

class movie(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=30)
    actor = models.CharField(max_length=50, default=None, null=True)
    explain = models.CharField(max_length=500, default=None, null=True)
    address = models.CharField(max_length=500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    movie = models.ForeignKey(movie, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
