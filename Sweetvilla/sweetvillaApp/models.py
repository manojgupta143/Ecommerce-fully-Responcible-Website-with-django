from django.db import models
from django.forms import CharField
from django.urls import reverse
class Product(models.Model):
    prodname=models.CharField(("product Name "), max_length=50)
    cetegory=models.CharField(("Cetegory"), max_length=60,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(("Description"), max_length=300)
    publish_date=models.DateField(("publishDate"))
    images=models.ImageField(("Images"), upload_to='EcommerceApp/images',default="")
    def __str__(self):
      return self.prodname
    def get_absolute_url(self):
        return reverse("ProductView", kwargs={"id": self.id})
#contact Model 

class Contact(models.Model):
  name=models.CharField(("Name "), max_length=30 ,default="")
  email=models.EmailField(("Email"), max_length=30 ,default="")
  phone = models.CharField(max_length=70, default="")
  detail=models.CharField(("Description"), max_length=500 ,default="")
  def __str__(self):
        return self.name



# Create your models here.

