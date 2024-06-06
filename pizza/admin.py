from django.contrib import admin

# Register your models here.


from .models import BaseModel,Authentication,Menu,Product,ProductExtra,ProductSize,About,Region,UsertLocation,Discount,Basket, LocationModel, AcsiyaModel, ContactModel, AdressCostumer


admin.site.register(LocationModel)
admin.site.register(AcsiyaModel)
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')


admin.site.register(AdressCostumer)
from pizza.models import (BaseModel,User,Menu,Product,
                          ProductExtra,ProductSize,About,Region,UsertLocation,
                          Discount,Basket,  Branche)

admin.site.register(BaseModel)
admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Product)
admin.site.register(ProductExtra)
admin.site.register(ProductSize)
admin.site.register(About)
admin.site.register(Region)
admin.site.register(UsertLocation)
admin.site.register(Discount)
admin.site.register(Basket)

admin.site.register(Branche)

