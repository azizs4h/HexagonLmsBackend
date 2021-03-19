from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
