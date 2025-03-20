from django.shortcuts import render,HttpResponse 
from .models import * 
from django.db.models import Count 

# Create your views here.
def index(request): 
    dataProduct = Product.objects.all() 
    dataSlideImage = SliderImage.objects.all() 
    dataPopularProduct = PopularProduct.objects.all() 
    dataCollection= Collection.objects.all() 
    dataPopularLocation = PopularLocation.objects.all() 
    dataServiceArea = ServiceArea.objects.all() 
    dataFooterTitle = FooterTitle.objects.all() 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    
    context = {
        'dataSlideImages' : dataSlideImage,
        'dataProducts' : dataProduct, 
        'dataPopularProducts' : dataPopularProduct, 
        'dataCollections' : dataCollection, 
        'dataPopularLocations' : dataPopularLocation, 
        'dataServiceAreas' : dataServiceArea, 
        'dataFooterTitles' : dataFooterTitle, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
        
    }
    return render(request,"shionhouse/index.html",context) 

# shop 
def shop(request): 
    dataProduct = Product.objects.all() 
    dataPopularProduct = PopularProduct.objects.all() 
    dataServiceArea = ServiceArea.objects.all() 
    dataFooterTitle = FooterTitle.objects.all() 
    dataProductType = ProductType.objects.all() 
    dataProductCategory = ProductCategory.objects.all() 
    dataProductColor = ProductColor.objects.all() 
    dataProductPriceRange = ProductPriceRange.objects.all() 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    context = {
        'dataProducts' : dataProduct, 
        'dataPopularProducts' : dataPopularProduct, 
        'dataServiceAreas' : dataServiceArea, 
        'dataFooterTitles' : dataFooterTitle, 
        'dataProductTypes' : dataProductType, 
        'dataProductCategorys' : dataProductCategory, 
        'dataProductColors' : dataProductColor, 
        'dataProductPriceRanges' : dataProductPriceRange, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
    }
    return render(request,'shionhouse/shop.html',context) 

# about 
def about(request): 
    dataPopularProduct = PopularProduct.objects.all() 
    dataServiceArea = ServiceArea.objects.all() 
    dataFooterTitle = FooterTitle.objects.all() 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataAboutTitle = AboutTitle.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    
    context = {
        'dataPopularProducts' : dataPopularProduct, 
        'dataServiceAreas' : dataServiceArea, 
        'dataFooterTitles' : dataFooterTitle, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
        'dataAboutTitles' : dataAboutTitle, 
    }
    return render(request,'shionhouse/about.html',context) 

# blog_details 
def blog_details(request,BlogId): 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataFooterTitle = FooterTitle.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    dataProductCategory = ProductCategory.objects.all() 
    dataBlogItem = BlogItem.objects.all() 
    dataBlogItemDetails = BlogItemDetails.objects.filter(id=BlogId)
    
    context = {
        'dataFooterTitles' : dataFooterTitle, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
        'dataProductCategorys' : dataProductCategory, 
        'dataBlogItems' : dataBlogItem, 
        'dataBlogItemDetailss' : dataBlogItemDetails, 
    }
    return render(request,'shionhouse/blog_details.html',context) 

# blog 
def blog(request): 
    dataFooterTitle = FooterTitle.objects.all() 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    dataBlogItem = BlogItem.objects.all() 
    dataProductCategory = ProductCategory.objects.all() 
    
    context = {
        'dataFooterTitles' : dataFooterTitle, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
        'dataBlogItems' : dataBlogItem, 
        'dataProductCategorys' : dataProductCategory, 
    }
    return render(request,'shionhouse/blog.html',context) 

# contact 
def contact(request): 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    dataFooterTitle = FooterTitle.objects.all() 
    dataMediaBodyContact = MediaBodyContact.objects.all() 
    dataContactWelcomeUs = ContactWelcomeUs.objects.all() 
    
    context = {
        'dataFooterTitles' : dataFooterTitle, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
        'dataMediaBodyContacts' : dataMediaBodyContact, 
        'dataContactWelcomeUss' : dataContactWelcomeUs, 
    }
    return render(request,'shionhouse/contact.html',context) 

# elements 
def elements(request): 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    dataFooterTitle = FooterTitle.objects.all() 
    
    context = {
        'dataFooterTitles' : dataFooterTitle, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
    }
    return render(request,'shionhouse/elements.html',context) 

# main 
def main(request): 
    return render(request,'shionhouse/main.html') 

# product_details 
def product_details(request,ProductId):  
    dataProductId = ProductId 
    dataImage = ProductImageDetail.objects.filter(productImageId=ProductId) 
    dataProductDetail = Product.objects.filter(id=ProductId) 
    dataPopularLocation = PopularLocation.objects.all() 
    dataServiceArea = ServiceArea.objects.all() 
    dataFooterTitle = FooterTitle.objects.all() 
    dataMenu = Menu.objects.annotate(sub_count = Count('submenus'))  
    dataSubMenu = SubMenu.objects.all() 
    dataSub2Menu = Sub2Menu.objects.all() 
    dataSocialMediaLink = SocialMediaLink.objects.all() 
    
    context = {
        'dataProductIds' : dataProductId, 
        'dataProductDetails' : dataProductDetail, 
        'dataImages' : dataImage, 
        'dataPopularLocations' : dataPopularLocation, 
        'dataServiceAreas' : dataServiceArea, 
        'dataFooterTitles' : dataFooterTitle, 
        'dataMenus' : dataMenu, 
        'dataSubMenus' : dataSubMenu, 
        'dataSub2Menus' : dataSub2Menu, 
        'dataSocialMediaLinks' : dataSocialMediaLink, 
    }
    return render(request,'shionhouse/product_details.html',context) 
