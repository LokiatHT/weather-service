from django.db import models
import uuid


class UserAPIKey(models.Model):
    api_key = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    usage_count = models.IntegerField(default=0)

    def increment_usage(self):
        self.usage_count += 1
        self.save()

    def is_valid(self):
        return self.usage_count < 3

class WeatherHistory(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C at {self.timestamp}"
