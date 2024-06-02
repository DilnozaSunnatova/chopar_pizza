from django.db import models

# Create your models here.
    
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
        return f"{self.id}-{self.name}"


class AcsiyaModel(models.Model):
    name = models.CharField(max_length=100)