from django.db import models

CATEGORIES = [('organic', 'organic'), ('furniture', 'furniture'), ('food', 'food'), ('cosmetics', 'cosmetics'), ('accessories', 'accessories')]

class Brand(models.Model):
    creator_id = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    creator_id = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORIES)
    price = models.IntegerField()
    image = models.TextField()
    brand_id = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name