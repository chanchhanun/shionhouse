from django.contrib import admin 
from .models import * 
from django.utils.html import format_html 

admin.site.site_header = "NUNTRA FASHION"
admin.site.site_title = "NUNTRA FASHION"
admin.site.index_title = "NUNTRA FASHION Admin Panel" 

# Register your models here. 

class AdminMenu(admin.ModelAdmin):
    list_display = [
        'menuName', 
    ] 
    list_filter = [
        'menuName', 
    ] 
    search_fields = [
        'menuName', 
    ]

class AdminFooterTitle(admin.ModelAdmin):
    list_display = [
        'title', 
        'SubTitle1', 
        'linkSub1', 
        'SubTitle2', 
        'linkSub2', 
        'SubTitle3', 
        'linkSub3', 
    ] 
    list_filter = [
        'title', 
        'SubTitle1', 
        'linkSub1', 
        'SubTitle2', 
        'linkSub2', 
        'SubTitle3', 
        'linkSub3', 
    ] 
    search_fields = [
        'title', 
        'SubTitle1', 
        'linkSub1', 
        'SubTitle2', 
        'linkSub2', 
        'SubTitle3', 
        'linkSub3', 
    ]
                                        
class AdminProductType(admin.ModelAdmin):
    list_display = [
        'types', 
        'productTypeDate', 
    ] 
    list_filter = [
        'types', 
        'productTypeDate', 
    ] 
    search_fields = [
        'types', 
    ]
                                        
class AdminProductCategory(admin.ModelAdmin):
    list_display = [
        'category', 
        'productCategoryDate', 
    ] 
    list_filter = [
        'category', 
        'productCategoryDate', 
    ] 
    search_fields = [
        'category', 
    ]
                                        
class AdminProductColor(admin.ModelAdmin):
    list_display = [
        'color', 
        'productColorDate', 
    ] 
    list_filter = [
        'color', 
        'productColorDate', 
    ] 
    search_fields = [
        'color', 
    ]
                                        
class AdminProductPriceRange(admin.ModelAdmin):
    list_display = [
        'priceRange', 
        'productPriceRangeDate', 
    ] 
    list_filter = [
        'priceRange', 
        'productPriceRangeDate', 
    ] 
    search_fields = [
        'priceRange', 
    ]
                                        
class AdminSocialMediaLink(admin.ModelAdmin):
    list_display = [
        'twitter', 
        'facebook', 
        'pinterest', 
    ] 
    list_filter = [
        'twitter', 
        'facebook', 
        'pinterest', 
    ] 
    search_fields = [
         'twitter', 
        'facebook', 
        'pinterest', 
    ]

class AdminProduct(admin.ModelAdmin):
    def image_preview(self,obj):
        if obj.productImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.productImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'id', 
        'productImage', 
        'productName', 
        'productTypeId', 
        'productCategoryId', 
        'productColorId', 
        'productPriceRangeId', 
        'productPrice', 
        'productOriginalPrice', 
        'discription', 
        'statusId', 
        'productDate', 
    ] 
    list_filter = ["productDate","productName","productPrice"]
    search_fields = ["productName","productPrice"]
    date_hierarchy = "productDate" 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 
    
class AdminProductImageDetail(admin.ModelAdmin):
    def image_preview(self,obj):
        if obj.productImageURL:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.productImageURL.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        "productImageId", 
        'id', 
            'productImageURL', 
        'productImageDate', 
    ] 
    list_filter = ["productImageDate"]
    search_fields = ["id"] 
    date_hierarchy = "productImageDate" 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 
    
class AdminStatus(admin.ModelAdmin): 
    list_display = [ 
        "id", 
        "statusName", 
    ] 
    list_filter = [
         "statusName", 
    ] 
    search_fields = [ 
        "id", 
        "statusName", 
    ] 
    
class AdminSlider(admin.ModelAdmin):
    def image_preview(self,obj):
        if obj.sliderImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.sliderImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        "heroCaption", 
        'id', 
        'sliderImage', 
    ] 
    search_fields = ["id","heroCaption"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 

class AdminPopularProduct(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.popularProductImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.popularProductImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'popularProductImage', 
        "popularProductCaption", 
        'id', 
    ] 
    search_fields = ["id","popularProductCaption"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 

class AdminCollection(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.collectionImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.collectionImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'collectionImage', 
        "collectionCaption", 
        'id', 
    ] 
    search_fields = ["id","collectionCaption"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 
    
class AdminPopularLocation(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.popularLocationImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.popularLocationImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'popularLocationImage', 
        "popularLocationCaption", 
        'id', 
    ] 
    search_fields = ["id","collectionCaption"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 
    
class AdminServiceArea(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.serviceAreaImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.serviceAreaImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'serviceAreaImage', 
        "serviceAreaTile", 
        "serviceAreaSubTitle", 
        'id', 
    ] 
    search_fields = ["id","serviceAreaTile","serviceAreaSubTitle"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 
    
class AdminAboutTitle(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.popularLocationImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.popularLocationImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'popularLocationImage', 
        "title", 
        "subTitle", 
        'id', 
    ] 
    search_fields = ["id","title","subTitle"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 

admin.site.register(ProductType,AdminProductType)
admin.site.register(ProductCategory,AdminProductCategory)
admin.site.register(ProductColor,AdminProductColor)
admin.site.register(ProductPriceRange,AdminProductPriceRange)
admin.site.register(Product,AdminProduct)
admin.site.register(ProductImageDetail,AdminProductImageDetail) 
admin.site.register(Status,AdminStatus) 
admin.site.register(SliderImage,AdminSlider) 
admin.site.register(PopularProduct,AdminPopularProduct) 
admin.site.register(Collection,AdminCollection) 
admin.site.register(PopularLocation,AdminPopularLocation) 
admin.site.register(ServiceArea,AdminServiceArea) 
admin.site.register(FooterTitle,AdminFooterTitle) 
admin.site.register(Menu,AdminMenu) 
admin.site.register(SubMenu) 
admin.site.register(Sub2Menu) 
admin.site.register(AboutTitle,AdminAboutTitle) 
admin.site.register(SocialMediaLink,AdminSocialMediaLink) 