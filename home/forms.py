from django import forms
from home.models import Mobile,Contact,Tag
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form for product adding
class MobileForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

# form for contact user
class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'  
 

# tag form for filteration
class TagForm(ModelForm):
    class Meta:
        model=Tag
        fields='__all__'                    
