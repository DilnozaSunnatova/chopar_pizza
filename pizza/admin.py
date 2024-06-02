from django.contrib import admin

# Register your models here.

from .models import LocationModel, AcsiyaModel, ContactModel


admin.site.register(LocationModel)
admin.site.register(AcsiyaModel)
admin.site.register(ContactModel)

