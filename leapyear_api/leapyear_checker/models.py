from django.db import models

class LeapYearHistory(models.Model):
    endpoint = models.CharField(max_length=10)
    input_data = models.CharField(max_length=255)
    result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.endpoint} - {self.input_data} - {self.created_at}"