from django.contrib import admin 
from .models import * 
from django.utils.html import format_html 
from import_export.admin import ExportActionMixin 

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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="1. Menu " 

class AdminSubMenu(admin.ModelAdmin):
    list_display = [
        'menuName', 
    ] 
    list_filter = [
        'menuName', 
    ] 
    search_fields = [
        'menuName', 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="1. Sub Menu  " 

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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="91. Footer " 
                                        
class AdminProductType(admin.ModelAdmin):
    list_display = [
        'types', 
        'productTypeDate', 
           'id', 
    ] 
    list_filter = [
        'types', 
        'productTypeDate', 
           'id', 
    ] 
    search_fields = [
        'types', 
           'id', 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="4. Product Type" 
                                        
class AdminProductCategory(ExportActionMixin,admin.ModelAdmin):
    list_display = [
        'category', 
        'productCategoryDate', 
        'id', 
    ] 
    list_filter = [
        'category', 
        'productCategoryDate', 
        'id', 
    ] 
    search_fields = [
        'category', 
        'id', 
    ] 
    
    resource_class = ExportProductCategory 

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="4. Product Category" 
                                        
class AdminProductColor(admin.ModelAdmin):
    list_display = [
        'color', 
        'productColorDate', 
           'id', 
    ] 
    list_filter = [
        'color', 
        'productColorDate', 
           'id', 
    ] 
    search_fields = [
        'color', 
           'id', 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="4. Product Color" 
                                        
class AdminProductPriceRange(admin.ModelAdmin):
    list_display = [
        'priceRange', 
        'productPriceRangeDate', 
           'id', 
    ] 
    list_filter = [
        'priceRange', 
        'productPriceRangeDate', 
           'id', 
    ] 
    search_fields = [
        'priceRange', 
           'id', 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="4. Product Price Range" 
                                        
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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="1. Socail Media Link " 

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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="4. Product " 
    
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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="4. Product ADetail" 
    
class AdminMediaBodyContact(admin.ModelAdmin): 
    list_display = [ 
        "id", 
        "houseName", 
        "houseLocation", 
        "phoneNumber", 
        "durationContact", 
        "email", 
        "emailTitle", 
    ] 
    list_filter = [
        "houseName", 
        "houseLocation", 
        "phoneNumber", 
        "durationContact", 
        "email", 
        "emailTitle", 
    ] 
    search_fields = [ 
        "id", 
         "houseName", 
        "houseLocation", 
        "phoneNumber", 
        "durationContact", 
        "email", 
        "emailTitle", 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="9. Contact " 
    
class AdminBlogItemDetails(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.blogItemImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.blogItemImage.url)
        return "No Image" 

    list_display = [ 
        "id", 
        "blogItemId", 
        "discription", 
        "blogTitleDetails", 
    ] 
    list_filter = [
        "blogItemId", 
        "discription", 
        "blogTitleDetails", 
    ] 
    search_fields = [ 
        "blogItemId", 
        "discription", 
        "blogTitleDetails", 
    ] 
    image_preview.short_discription = "Image Preview" 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="8. Blog Detail " 

    
class AdminStatus(admin.ModelAdmin): 
    list_display = [ 
        "statusName", 
        "id", 
    ] 
    list_filter = [
         "statusName", 
    ] 
    search_fields = [ 
        "id", 
        "statusName", 
    ] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="4. Product Status " 
    
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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="2. Sliders" 
    
    
class AdminContactWelcomeUs(admin.ModelAdmin):
    def image_preview(self,obj):
        if obj.welcomeUsImageURL:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.welcomeUsImageURL.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'id', 
    ] 
    search_fields = ["id"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="9. Contact Picture " 

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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="3. Product Popular" 

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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="5. Collection-1" 
    
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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="5. Collection-2" 
    
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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="6. Service Area" 
    
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
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="7. About " 
    
class AdminBlogItem(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.blogItemImage:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.blogItemImage.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        'blogItemImage', 
        "dayDate", 
        "monthDate", 
        "infoTitle", 
        "title", 
        "subTitle", 
        'id', 
    ] 
    search_fields = ["id","title","subTitle","dayDate","monthDate","infoTitile"] 
    image_preview.short_discription = "Image Preview" 
    readonly_fields = ["image_preview"] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="8. Blog " 
    
class AdminLogoUpdate(admin.ModelAdmin): 
    def image_preview(self,obj):
        if obj.logoBlack:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.logoBlack.url)
        return "No Image" 
    def image_preview2(self,obj):
        if obj.logoWhite:
            return format_html('<img src="/static{}" width="100" height="auto" >',obj.logoWhite.url)
        return "No Image" 
    list_display = [ 
        "image_preview", 
        "image_preview2", 
        'id', 
    ] 
    search_fields = ["id","title" ] 
    image_preview.short_discription = "Image Preview" ,"Image Preview2" 
    readonly_fields = ["image_preview","image_preview2"] 
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.opts.verbose_name_plural="1. Update Logo" 

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
admin.site.register(SubMenu,AdminSubMenu) 
# admin.site.register(Sub2Menu) 
admin.site.register(AboutTitle,AdminAboutTitle) 
admin.site.register(SocialMediaLink,AdminSocialMediaLink) 
admin.site.register(BlogItem,AdminBlogItem) 
admin.site.register(BlogItemDetails,AdminBlogItemDetails) 
admin.site.register(MediaBodyContact,AdminMediaBodyContact) 
admin.site.register(ContactWelcomeUs,AdminContactWelcomeUs) 
admin.site.register(LogoUpdate,AdminLogoUpdate) 
