
from webbrowser import get
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from home.models import Mobile,Order,OrderItem,Product,Customer,User
from home.forms import MobileForm,ContactForm,TagForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django import forms
from django.urls import reverse_lazy,reverse
import requests
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ValidationError
from django.views import View
from django.views.generic import DetailView


# Create your views here.

# User can register here

def signup(request):
    if request.method=="GET":
        return render(request,'register.html')    
    else:
        name=request.POST.get('name')   
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        # print(name, email, password,request.method)
        #validation
        customer=Customer(name=name,email=email,pswd=pswd) 
        value={'name':name,
        'email':email,

        }
        error_message=None
        if(not name):
            error_message="Name is required!!" 
        elif len(name)<4:
            error_message="name should be more than 4 letters"    

        if(not email):
            error_message="Email is required!!" 
        elif(len(email)<13):
            error_message="email must be more than 4 letters"    
        
        if(not pswd):
            error_message="password is required!!" 
        elif len(pswd)<4:
            error_message="Password should be more than 4 letters"  
        
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'

        if (not error_message):    

            customer.pswd=make_password(customer.pswd) 

            customer.save()
       
        else:    
            context={
            'error':error_message,
            'values':value
               }
            return render(request,'register.html',context)       
    return render(request,'register.html')    
    
#  function for login user
def loginUser(request):
    if request.method=='get':
        return render(request,'login.html')
    else:
         email=request.POST.get('email')
         pswd=request.POST.get('pswd')
         customer=Customer.get_customer_by_email(email)
         if customer:
            Flag=check_password(pswd,customer.pswd)
            if Flag:
                messages.add_message(request, messages.INFO, "Thank You " +customer.name +', You have successfully logged in')
                return redirect("/")
            else:
                error_message="email or password is incorrect"
         else:
            error_message="Email or password in incorrect"
            print(error_message)
         return render(request,'login.html',{'error':error_message})
        #  user=authenticate(name=name,pswd=pswd)
        #  if user is not None:
        #     login(request,user)
        #     return redirect("/")

        #  else:
         return render(request,'login.html')

# this is function for contact us page
# try:  
def mobile_like(request,pk):
    # mobile_id=request.POST.get('mobile_id')
    # mobile=Mobile.objects.get('idd=mobile.id')
    # customer=Customer.objects.get('customer')
    # if not Customer.objects.filter(customer=customer):
    #     Customer.objects.create(customer=customer)
    # if mobile.like.filter(id=Customer.objects.get(custome=customer).id).exists(): 
    #     mobile.like.remove(Customer.objects.get(customer=customer))  
    # else:
    #     mobile.like.add(Customer.objects.get(customer=customer))



    mobile=get_object_or_404(User,id=request.POST.get('mobile_id'))
    mobile.like.add(request.user)
    return HttpResponseRedirect(reverse('mobile_details',args=[str(pk)]))
    

def logout(request):
    request.session.clear()
    return redirect('login')

@login_required
def contact(request):
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if(form.is_valid()):
                print("validated")
                form.save()
                messages.add_message(request, messages.INFO, 'This is done')
                return redirect("/")
               
        else:
                print(form.errors)
                messages.add_message(request, messages.INFO, 'some error ')      
    context={'form':form}    
    return render(request,'contact.html',context)

#  for home page where product listing will show
# @login_required

def index(request):  
       detail=Mobile.objects.all()
       context={'detail':detail}
       return render(request,'show_list.html',context) 

class MobileDetailView(View):
    model = Customer
    context_object_name = 'mobile'
    template_name = 'mobile_details.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # adding like count
        like_status = False
        customer = Customer.objects.get(customer=customer)
        if self.object.likes.filter(id=Mobile.objects.get(customer=customer).id).exists():
            like_status = True
        else:
            like_status=False
        context['like_status'] = like_status


        return self.render_to_response(context)        


# To show the particular mobile details 
def mobile_details(request,idd):
    mobile=Mobile.objects.get(id=idd)
    return render(request,'mobile_details.html',{'mobile':mobile}) 

#  adding a product to cart 
def add_to_cart(request):
    cart=OrderItem.objects.all()
    context={'cart':cart}
    return render(request,'add_to_cart.html',context)    


# This is for filtering a phone on the basis of tag
def tag(request):
    form=TagForm()
    if(request.method=='POST'):
        form=TagForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'tagform.html')
        else:
            return render(request,'tagform.html')
    else:
        return render(request,'tagform.html')         


#  To logout user
def logoutUser(request):
     logout(request)
     return redirect('/index')

#Only for admin    
def phone_entry_form(request,slug):
    form=MobileForm()
    mobile=Mobile.objects.get(slug=slug)
    if request.method=="POST":
        if request.user_is_authenticated:
            user=request.user
            mobile.like.add(user)
        form=MobileForm(request.POST,request.FILES)
        if(form.is_valid()):

                print("validated")
                form.save()
                messages.add_message(request, messages.INFO, 'This is done')
                return redirect("/")         
        else:
                print(form.errors)
                messages.add_message(request, messages.INFO, 'some error ')      
    context={'form':form}    
    return render(request,'entry_form.html',context)    

# to delete an item from listing page by ad,in only
def delete(request,idd):
    Mobile.objects.get(id=idd).delete()
    return redirect('index.html/')
# remove an item from cart
def deleteitem(request,idd):
    OrderItem.objects.get(id=idd).delete()
    return redirect('add_to_cart.html/')    
# to show profile details of user ( user can view their on data )
def profile(request):
    return render(request,'profile.html')  

# This is for about us page ( You can add more details about the company )
def about(request):
    return render(request,'about.html') 

def homepage(request):
    return render(request,'homepage.html')     

def load_products(request):
    r = requests.get('https://fakestoreapi.com/products')
    for item in r.json():
        product = Product(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            image_url=item['image']
        )
        product.save()

    return render(request, 'index.html')    


def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products, 
            key=lambda x: request.session['recently_viewed'].index(x.id)
            )
        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True

    context = {'product': product, 'recently_viewed_products': recently_viewed_products}
    return render(request, 'product.html', context)    

