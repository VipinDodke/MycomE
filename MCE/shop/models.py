from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    Price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    pud_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    def __str__(self) :
        return self.product_name
class Contect(models.Model):
    msg_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, default="")
    City= models.CharField(max_length=60, default="")
    Call = models.IntegerField(max_length=14,default=0)
    desc = models.CharField(max_length=1100)
    State = models.CharField(max_length=50)
    Zip = models.IntegerField(max_length=14,default=0)
    def __str__(self) :
        return self.Name