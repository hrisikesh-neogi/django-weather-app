from django.db import models

# Create your models here.
from django.db import models

class WeatherSearchHistory(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.CharField(max_length=255)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search in {self.city} at {self.search_time.strftime('%Y-%m-%d %H:%M:%S')}"
