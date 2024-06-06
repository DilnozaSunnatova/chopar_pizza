from django.db import models
from django.contrib.auth.base_user import  BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.apps import apps
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib import auth




class PhoneManager(BaseUserManager):
    use_in_migrations = True

    def normalize_phone(self, phone):
     
        return phone.strip()

    def _create_user(self, phone, email, password=None, **extra_fields):
        
        if not phone:
            raise ValueError("Telefon raqami kiritilishi shart")
        email = self.normalize_email(email)
        phone = self.normalize_phone(phone)
        user = self.model(phone=phone, email=email ,**extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser bo'lishi uchun is_staff=True bo'lishi kerak.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser bo'lishi uchun is_superuser=True bo'lishi kerak.")

        return self._create_user(phone, email, password, **extra_fields)

@deconstructible
class UnicodePhoneValidator(validators.RegexValidator):
    regex = r"^998[0-9]{9}"
    message = "Noto'g'ri raqam"



class User(AbstractUser):
    class UserAuthStatus(models.TextChoices):
        NEW = 'new', 'Yangi'
        APPROVED = 'approved', 'Tasdiqlangan'

    class GenderStatus(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
    phone_validator = UnicodePhoneValidator()
    phone = models.CharField(max_length=20,unique= True, validators=[phone_validator],null=True)
    username = None
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = PhoneManager()
    status = models.CharField(max_length=50,choices=UserAuthStatus.choices, default='new')

    code = models.CharField(max_length=4,null=True)
    expire_date = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(
        max_length=200,
        choices=GenderStatus.choices
    )
    birth_date = models.DateField(null=True)
    name = models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return str(self.name)         


class BaseModel(models.Model):
    created_up = models.DateField()
    updated_up = models.DateField()




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

class Discount(models.Model):
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
    















































    












