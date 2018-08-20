from django.db import models

class Advertisment(models.Model):
    accommodation_name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.accommodation_name
