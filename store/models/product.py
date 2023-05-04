from django.db import models
class Products(models.Model):
    title = models.CharField(max_length=60)
    price_detail_amount= models.IntegerField(default=0)
    url= models.CharField(max_length=250, default='', blank=True, null= True)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()
