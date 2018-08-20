from django.db import models

class Advertisement(models.Model):
    accommodation_name = models.CharField(max_length=50)
    base_price = models.IntegerField(default=0)

    def __str__(self):
        return self.accommodation_name
