#from _typeshed import Self
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.
STATE_CHOICES=(
    ('Andhra Pradesh','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chhatisgarh'),
    ('Punjab','Punjab')
)

class Customer(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

#def _str_(Self):
    #return str(self.id)

CATEGORY_CHOICES=(
    ('PA','Paintings'),
    ('HO','Home Decor'),
    ('JE','Jewellery')
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.IntegerField()
    description=models.TextField(max_length=500)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=50)
    product_image=models.ImageField(upload_to='media\productimg')

#def _str_(Self):
    #return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=CASCADE)
    quantity=models.IntegerField(default=1)

#def _str_(Self):
    #return str(self.id)

class Orderplaced(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    quantity=models.IntegerField()
    status=models.CharField(max_length=50)

