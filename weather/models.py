from django.db import models

class WeatherHistory(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C at {self.timestamp}"
