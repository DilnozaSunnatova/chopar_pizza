from django.contrib import admin
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

