from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views
# from .views import MobileDetailView

urlpatterns = [
    path('',views.index,name='index'),
    path('phone_form/',views.phone_entry_form,name='phone_entry_form'), 
    # path('delete/<int:idd>',views.delete,name='delete'),               // admin can delete any item 
    path('deleteitem/<int:idd>',views.deleteitem,name='deleteitem'),
    path('loginpage/',views.loginUser,name='loginpage'),
    path('homepage/',views.homepage,name='homepage'),
    path('logout/',views.logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('signup',views.signup,name='signup'),
    path('tag/',views.tag,name='tag'),
    path('mobile_details/<int:idd>',views.mobile_details,name='mobile_details'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('about/',views.about,name='about'),
    path('product/<int:product_id>',views.product,name='product'),
    # path('index1/',views.index1,name='index1'),
    path('mobile_like/<int:pk>',views.mobile_like, name='mobile_like')




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)