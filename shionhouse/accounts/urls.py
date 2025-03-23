from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name="index"), 
    path('shop/',views.shop,name="shop"), 
    path('about/',views.about,name="about"), 
    path('blog/',views.blog,name="blog"), 
    path('contact/',views.contact,name="contact"), 
    path('elements/',views.elements,name="elements"), 
    # path('<path:anything>/', views.routeNotFound, name="routeNotFound"),
    # path('main/',views.main,name="main"), 
    path('shop/product_details/<int:ProductId>/',views.product_details,name="product_details"), 
    path('blog/blog_details/<int:BlogId>/',views.blog_details,name="blog_details"), 
] 

