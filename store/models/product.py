from django.db import models
from .category import Category
class Products(models.Model):
    title = models.CharField(max_length=60)
    price_detail_amount= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    url= models.CharField(max_length=250, default='', blank=True, null= True)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryname(category_name):
        if category_name:
            return Products.objects.filter (category=category_name)
        else:
            return Products.get_all_products();