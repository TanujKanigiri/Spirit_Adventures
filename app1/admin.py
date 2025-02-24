from django.contrib import admin
from .models import *

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=['name']
    
class sub_categoryAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(category,categoryAdmin)
admin.site.register(sub_category,sub_categoryAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'package', 'submitted_at']
admin.site.register(Contact,contactAdmin)


class packageAdmin(admin.ModelAdmin):
    list_display=['city','package_image','package_name','discount_price','full_price','Availability','no_of_days']

admin.site.register(packages,packageAdmin)

class citypageAdmin(admin.ModelAdmin):
    list_display=['city_name','city_image','city_description','city_gallery1','city_gallery2','city_gallery3','city_gallery4','city_gallery5','city_map']
    
admin.site.register(Basecitypage,citypageAdmin)

class packagedetailsAdmin(admin.ModelAdmin):
    list_display=['package','cityheading','city_sub_desc','video1','source','destination','region','temperature1','temperature2','eventcost','flashsaleprice','couplesharingcost','place1heading','place1description','place2heading','place2description','place3heading','place3description','place4heading','place4description','staysheading','staysdescription','totalcost','meetingpointcity','image1','image2','image3','image4','image5','image6']
    
admin.site.register(Package_details,packagedetailsAdmin)

class packagedetailsAdmin2(admin.ModelAdmin):
    list_display=['day']

admin.site.register(package_details_category,packagedetailsAdmin2)

class packagedetailssubAdmin(admin.ModelAdmin):
    list_display=['t1','t2','t3','t4','text','pid']

admin.site.register(package_details_sub,packagedetailssubAdmin)