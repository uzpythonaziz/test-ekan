from django.db import models
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=500,help_text="Bu yerda kategotiya yozing")
    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    desc=models.TextField()
    image=models.ImageField(upload_to='products')
    cost=models.IntegerField()
    def __str__(self):
        return self.name