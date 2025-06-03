from django.db import models
from django.contrib.auth.models import User

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()

    class Meta:
        verbose_name_plural = "Search Histories"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.city} - {self.timestamp}"

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Favorite Cities"
        unique_together = ['user', 'city']

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.city}"
