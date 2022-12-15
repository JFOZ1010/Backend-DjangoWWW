from django.db import models

# Create your models here.
class New(models.Model):
    new_id = models.AutoField(primary_key=True)
    new_title = models.CharField(max_length=25)
    prueba = models.IntegerField(max_length=25, null=True)
    new_date = models.DateField(auto_now_add=True)
    new_image = models.CharField(max_length= 500)
    new_description = models.TextField()



class Account(models.Model):
    user_id = models.CharField(primary_key = True, max_length = 200)
    user_type = models.IntegerField()
    password = models.CharField(max_length = 20)
    email = models.EmailField()
    user_status = models.BooleanField(default = True)

    
class Supplier(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name= 'supplier', primary_key = True)
    supplier_name = models.CharField(max_length = 30)
    
class User(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name= 'user', primary_key = True)
    user_type = models.IntegerField()
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    birth_date = models.DateField()
    sex = models.CharField(max_length = 20)

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
    user_id = models.ForeignKey(Supplier, max_length=25, on_delete=models.CASCADE)
    item_price = models.IntegerField()
    item_picture = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_url = models.CharField(max_length=100)
    
    
class History_item(models.Model):
    history_id = models.ForeignKey(History, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('history_id', 'item_id'))