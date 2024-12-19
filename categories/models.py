from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
