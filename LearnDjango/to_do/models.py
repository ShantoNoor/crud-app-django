from django.db import models

# Create your models here.
class TodoList(models.Model):
    STATUS_CHOICES = [
        ('F', 'Finished'),
        ('R', 'Running'),
        ('W', 'Waiting'),
    ]

    title = models.CharField(max_length=256)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='W')

    def __str__(self):
        return self.title