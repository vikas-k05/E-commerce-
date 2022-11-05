from django.contrib import admin

from home.models import Mobile,Contact,Tag,Customer,Order,OrderItem,ShippingAddress

# Register your models here.
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display=['id','phone','brand','ram','color']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin): 
    list_display= ['id','name','city','mob_no']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin): 
    list_display= ['id','name','email']    


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin): 
    list_display= ['id','tag'] 

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ShippingAddress)