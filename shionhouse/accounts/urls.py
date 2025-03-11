from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name="index"), 
    path('shop/',views.shop,name="shop"), 
    path('about/',views.about,name="about"), 
    path('blog_details/',views.blog_details,name="blog_details"), 
    path('blog/',views.blog,name="blog"), 
    path('contact/',views.contact,name="contact"), 
    path('elements/',views.elements,name="elements"), 
    path('main/',views.main,name="main"), 
    path('product_details/<int:ProductId>/',views.product_details,name="product_details"), 
] 
