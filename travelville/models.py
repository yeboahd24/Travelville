from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to="places")
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title
