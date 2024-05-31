from django.db import models

class BaseModel(models.Model):
    created_up = models.DateTimeField()
    updated_up = models.DateTimeField()

class Category(models.Model):
    name = models.CharField(max_length=30)

class Extra(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='extra')
    price = models.DecimalField(max_digits=10, decimal_places= 2)

class Size(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places= 2)

class Product(BaseModel):
    name = models.CharField(max_length= 30)
    image = models.ImageField(upload_to='product')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    size = models.CharField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size,null=True, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE)









