from django.db import models

    
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point

class LocationModel(models.Model):
    name = models.CharField(max_length=100)
    # coordinates = models.PointField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    customer_number = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class AcsiyaModel(models.Model):
    name = models.CharField(max_length=100)
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
    def __str__(self) -> str:
        return self.first_name

class Menu(models.Model):
    name = models.CharField(max_length=30)



    def __str__(self) -> str:
        return self.name
    
class ProductExtra(models.Model):
    image = models.ImageField(upload_to='extra')
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    name = models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.name
    
class ProductSize(models.Model):
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    # product = models.ForeignKey(Product,on_delete=models.CASCADE )
    # extra_products = models.ManyToManyField(ProductExtra,default=None)


    def __str__(self) -> str:
        return self.size



class Product(BaseModel):
    name = models.CharField(max_length= 30)
    photo = models.ImageField(upload_to='product1')
    description = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    status = models.BooleanField()
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name








class About(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self) -> str:
        return self.name



class Region(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name



class UsertLocation(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    podyezd = models.IntegerField()
    code = models.IntegerField()
    adress_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.adress


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    link = models.URLField()
    description = models.TextField()
    order_numbere = models.CharField(max_length=10)
    review = models.TextField()


    def __str__(self) -> str:
        return self.name

class Discount(BaseModel):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='discount')
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Basket(models.Model):
    img = models.ImageField(upload_to='basket')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    number = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places= 2)

    def __str__(self) -> str:
        return self.name






#  Buni Abdulloh aka qilgan ekan men qo'shish uchun qilgandim o'chirsalariz bo'ladi
class Product(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

# Card Item bu hamma mahsulotlarni yig'ib beradi o'chirmanglar
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.product.price * self.quantity


class AdressCostumer(models.Model):
    latitude = models.FloatField(null=True) 
    longitude = models.FloatField(null=True)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    kvartira = models.CharField(max_length=150)
    podez = models.CharField(max_length=150)
    enter_code = models.IntegerField()
    dom = models.PositiveIntegerField(default=1)
    