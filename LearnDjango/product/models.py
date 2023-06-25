from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=1000)
    is_available = models.BooleanField(default=True)
    available_qty = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title