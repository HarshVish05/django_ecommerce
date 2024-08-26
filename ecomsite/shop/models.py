from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length= 200)
    price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length= 200)
    image = models.CharField(max_length= 400)
    
    
    def __str__(self):
        return self.title
