from django.db import models

class Nifty_Data(models.Model):
    BANKNIFTY = models.CharField(max_length=150)
    DATE = models.DateField(blank=True)
    TIME = models.CharField(max_length=50)
    OPEN = models.CharField(max_length=150)
    HIGH = models.CharField(max_length=150)
    LOW = models.CharField(max_length=150)
    CLOSE = models.CharField(max_length=150)
    VOLUME = models.CharField(max_length=150)
    def __str__(self):
        return self.BANKNIFTY
