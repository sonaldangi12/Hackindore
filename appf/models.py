from django.db import models

class feed_back(models.Model):
    email = models.EmailField(max_length=100)
    msg = models.CharField(max_length=1000)

    def __str__(self):
        return self.email