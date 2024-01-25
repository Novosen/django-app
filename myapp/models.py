from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, default="N/D")

    def __str__(self):
        return self.name

