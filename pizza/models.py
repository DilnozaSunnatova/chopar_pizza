from django.db import models

class BaseModel(models.Model):
    created_up = models.DateTimeField()
    updated_up = models.DateTimeField()

class User(BaseModel):
    class GenderStatus(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    birt_date = models.DateField()
    gender = models.CharField(
        max_length=20,
        choices=GenderStatus.choices
    )


class Category(models.Model):
    name = models.CharField(max_length=30)

class Product(BaseModel):
    name = models.CharField(max_length= 30)
    image = models.ImageField(upload_to='product')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField()

class ProductExtra(models.Model):
    
    image = models.ImageField(upload_to='extra')
    price = models.DecimalField(max_digits=10, decimal_places= 2)

class ProductSize(models.Model):
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    product = models.CharField(max_length=30)
    extra_products = models.ManyToManyField(ProductExtra,)

class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


# class UsertLocation(models.Model):
    

    


class Discount(BaseModel):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='discount')
    description = models.TextField()


class Basket(models.Model):
    img = models.ImageField(upload_to='basket')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    number = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places= 2)








