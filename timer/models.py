from django.db import models

# Create your models here.

class Timer(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    is_running = models.BooleanField(default=False)
    elapsed_time = models.FloatField(default=0.0) # Saniye olarak saklanır

    def __str__(self):
        return f"Timer - {self.elapsed_time:.2f} seconds"