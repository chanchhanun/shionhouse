from django.db import models 

# Create your models here. 

class Menu(models.Model): 
    menuName = models.CharField(max_length=200,null=True) 
    url = models.CharField(max_length=200,null=True) 
    
    def __str__(self):
        return f'{self.menuName}' 

class SubMenu(models.Model): 
    menuName = models.CharField(max_length=200,null=True) 
    url = models.CharField(max_length=200,null=True) 
    menuId= models.ForeignKey(Menu,on_delete=models.CASCADE,null=True,related_name='submenus') 
    def __str__(self): 
        return f'{self.menuId.menuName} -> {self.menuName}' 

class Sub2Menu(models.Model): 
    menuName = models.CharField(max_length=200,null=True) 
    url = models.CharField(max_length=200,null=True) 
    menuId= models.ForeignKey(SubMenu,on_delete=models.CASCADE,null=True) 
    def __str__(self):
        return f'{self.menuId.menuName} -> {self.menuName}' 
    
    
class Status(models.Model): 
    statusName = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return f'{self.statusName}' 
    
class ProductType(models.Model):  
    types = models.CharField(max_length=200,null=True)
    productTypeDate = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return f'{self.types}'
    
class ProductCategory(models.Model):  
    category = models.CharField(max_length=200,null=True)
    productCategoryDate = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return f'{self.category}'
    
class ProductColor(models.Model):  
    color = models.CharField(max_length=200,null=True)
    productColorDate = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return f'{self.color}' 
    
class ProductPriceRange(models.Model):  
    priceRange = models.CharField(max_length=200,null=True)
    productPriceRangeDate = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return f'{self.priceRange}' 

class Product(models.Model):
    productName = models.CharField(max_length=200,null=True) 
    productTypeId = models.ForeignKey(ProductType,on_delete=models.CASCADE,null=True) 
    productCategoryId = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True) 
    productColorId = models.ForeignKey(ProductColor,on_delete=models.CASCADE,null=True) 
    productPriceRangeId = models.ForeignKey(ProductPriceRange,on_delete=models.CASCADE,null=True) 
    productPrice =  models.CharField(max_length=200,null=True) 
    productOriginalPrice = models.CharField(max_length=200,null=True) 
    productImage = models.ImageField(upload_to='product_image/',null=True,blank=True) 
    discription  = models.CharField(max_length=500,null=True) 
    statusId = models.ForeignKey(Status,on_delete=models.CASCADE,null=True) 
    productDate = models.DateField(auto_now_add=True,null=True) 
    def __str__(self):
        return f'{self.productName} | {self.id}' 

class ProductImageDetail(models.Model): 
    productImageId = models.ForeignKey(Product,on_delete=models.CASCADE,null=True) 
    productImageURL = models.ImageField(upload_to='product_image_detial/',null=True,blank=True) 
    productImageDate = models.DateField(auto_now_add=True,null=True) 
    def __str__(self): 
        return f'{self.productImageId} | {self.productImageURL}' 
    
class SliderImage(models.Model): 
    sliderImage = models.ImageField(upload_to='slider_images/',null=True,blank=True) 
    heroCaption = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return f'{self.id} | {self.sliderImage} | {self.heroCaption}' 
    
class PopularProduct(models.Model): 
    popularProductImage = models.ImageField(upload_to='popular_product/',null=True,blank=True) 
    popularProductCaption = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return f'{self.popularProductImage} | {self.popularProductCaption}' 

class Collection(models.Model): 
    collectionImage = models.ImageField(upload_to='collection_image/',null=True,blank=True) 
    collectionCaption = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return f'{self.id} | {self.collectionCaption} | {self.collectionImage}' 

class PopularLocation(models.Model): 
    popularLocationImage = models.ImageField(upload_to='popular_location/',null=True,blank=True) 
    popularLocationCaption = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return f'{self.popularLocationCaption} | {self.popularLocationImage}' 

class ServiceArea(models.Model): 
    serviceAreaImage = models.ImageField(upload_to='service_area/',null=True,blank=True) 
    serviceAreaTile = models.CharField(max_length=200,null=True) 
    serviceAreaSubTitle = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return f'{self.serviceAreaImage} | {self.serviceAreaTile} | {self.serviceAreaSubTitle}' 

class FooterTitle(models.Model): 
    title = models.CharField(max_length=200,null=True) 
    SubTitle1 = models.CharField(max_length=200,null=True) 
    linkSub1 = models.CharField(max_length=200,null=True) 
    SubTitle2 = models.CharField(max_length=200,null=True) 
    linkSub2 = models.CharField(max_length=200,null=True) 
    SubTitle3 = models.CharField(max_length=200,null=True) 
    linkSub3 = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return f'{self.title} | {self.SubTitle1} | {self.linkSub1} | {self.SubTitle2} | {self.linkSub2} | {self.SubTitle3} | {self.linkSub3}' 

