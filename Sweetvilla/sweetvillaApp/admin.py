from django.contrib import admin
from.models import Product,Contact
class productadmin(admin.ModelAdmin):
   pass

# Register your models here.
class contactAdmin(admin.ModelAdmin):
   pass

admin.site.register(Product,productadmin)
admin.site.register(Contact,contactAdmin)

# Register your models here.
