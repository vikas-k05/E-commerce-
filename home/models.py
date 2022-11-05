from re import L
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#this  model  is for filter
class Tag(models.Model):
    tag=models.CharField(max_length=20)
    profile=models.ImageField(upload_to='media/images/',null=True,default=None)
    def __str__(self):
        return self.tag        



# This is a model by which anyuser can fill details to contact with us  
class Contact(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)      
    mob_no=models.IntegerField()  
    message=models.CharField(max_length=500)  
    def __str__(self):
        return self.name

#  to add anew customer
class Customer(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    pswd=models.CharField(max_length=20,null=True)
    


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            False    
        

    def isExists(self):
       if Customer.objects.filter(email = self.email):
            return True

       return  False


# Order model
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)    

# This is address of any customer
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address 






# this is a product model 
class Mobile(models.Model):
    phone=models.CharField(max_length=50)
    brand=models.CharField(max_length=20)
    ram=models.CharField(max_length=10)
    color=models.CharField(max_length=20)
    image=models.ImageField(upload_to='media/images/',null=True,default=None)
    price=models.CharField(max_length=5,null=True)
    date=models.DateField(null=True,default=None)
    tags=models.ManyToManyField(Tag,default=None)
    like=models.ManyToManyField(Customer,related_name='mobiles',blank=True, null=True,default=None)
    def __str__(self):
        return self.phone   

    def total_like(self):
        return self.like.count()         

# order item model for cart 
class OrderItem(models.Model):
    product = models.ForeignKey(Mobile, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    # price=models.OneToOneField(Mobile,on_delete=models.SET_NULL,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total      

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=100)             
