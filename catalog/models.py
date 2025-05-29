from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
import uuid

class TypeProduct(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    discount = models.FloatField(
    validators=[MinValueValidator(limit_value=0.0),MaxValueValidator(limit_value=100.0)])
    type_product = models.ForeignKey(TypeProduct,on_delete=models.CASCADE)
    c_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    path = models.ImageField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)






