from django.db import models
from django.utils import timezone

class ChaiVariety(models.Model):
    CHAI_TYPE = [
        ('MT', 'MASALA TEA'),
        ('LT', 'LEMON TEA'),
        ('NT', 'NORMAL TEA'),
        ('BT', 'BLACK TEA'),
    ]

    image = models.ImageField(upload_to='chais/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE)

    def __str__(self):
        return self.name