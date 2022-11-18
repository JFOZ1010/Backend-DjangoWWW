# Create your models here.
from django.db import models

# Create your models here.
class New(models.Model):
    new_id = models.AutoField(primary_key=True)
    new_title = models.CharField(max_length=25)
    new_date = models.DateField(auto_now_add = True)
    new_image = models.CharField(max_length= 500)
    new_description = models.CharField(max_length= 300)

class Account(models.Model):
    user_id = models.CharField(max_length = 200)
    user_type = models.IntegerField()
    password = models.CharField(max_length = 20)
    email = models.EmailField()

    class Meta:
        unique_together = (('user_id', 'user_type'))
    
class Supplier(models.Model):
    supplier_id = models.CharField(max_length = 200, primary_key = True)
    supplier_name = models.CharField(max_length = 30)
    email = models.EmailField()
    
class User(models.Model):
    user_id = models.CharField(max_length = 200)
    user_type = models.IntegerField()
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    birth_date = models.DateField()
    sex = models.CharField(max_length = 20)

    class Meta:
        unique_together = (('user_id', 'user_type'))
    
class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    item_date = models.DateField()
    item_price = models.CharField(max_length=50)

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length= 25)

class Item(models.Model): 
    item_id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    supplier_id = models.ForeignKey(Supplier, max_length=25, on_delete=models.CASCADE)
    item_price = models.IntegerField()
    item_picture = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_url = models.CharField(max_length=100)
    
    
class History_item(models.Model):
    history_id = models.ForeignKey(History, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('history_id', 'item_id'))




"""INICIA BLOQUE DE CRUD DE NOTICIA"""

"""FIN BLOQUE DE CRUD DE NOTICIA"""

