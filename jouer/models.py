from django.db import models

class mot(models.Model):
    text = models.CharField(max_length=25)

    def __str__(self):
        return self.text

