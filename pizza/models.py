from django.db import models

class BaseModel(models.Model):
    created_up = models.DateTimeField()
    updated_up = models.DateTimeField()

class Authentication(BaseModel):
    class GenderStatus(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    first_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13)
    birt_date = models.DateField()
    gender = models.CharField(
        max_length=20,
        choices=GenderStatus.choices
    )


class Menu(models.Model):
    name = models.CharField(max_length=30)

class ProductExtra(models.Model):
    image = models.ImageField(upload_to='extra')
    price = models.DecimalField(max_digits=10, decimal_places= 2)


class Product(BaseModel):
    name = models.CharField(max_length= 30)
    photo = models.ImageField(upload_to='product1')
    description = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    status = models.BooleanField()
    # size1 = models.ForeignKey(ProductSize, on_delete=models.CASCADE, null=True)


class ProductSize(models.Model):
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    product = models.ForeignKey(Product,on_delete=models.CASCADE )
    extra_products = models.ManyToManyField(ProductExtra,)





class About(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()



class Region(models.Model):
    name = models.CharField(max_length=30)



class UsertLocation(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    podyezd = models.IntegerField()
    code = models.IntegerField()
    adress_name = models.CharField(max_length=200)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    link = models.URLField()
    description = models.TextField()
    order_numbere = models.CharField(max_length=10)
    review = models.TextField()





    





    

    


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








