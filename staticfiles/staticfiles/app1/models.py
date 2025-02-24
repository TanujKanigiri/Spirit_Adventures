from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class userinfoModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=150)
    message=models.CharField(max_length=150)

class feedback(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    feedback=models.CharField(max_length=200)

class category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class sub_category(models.Model):
    name=models.CharField(max_length=100)
    cid = models.ForeignKey(
        category, 
        on_delete=models.CASCADE, 
        blank=False,
        related_name='subcategories'
    )
    def __str__(self):
        return self.name

class Basecitypage(models.Model):
    city_name=models.CharField(max_length=50)
    city_image=CloudinaryField('image')
    city_description=models.TextField()
    city_gallery1=CloudinaryField('image')
    city_gallery2=CloudinaryField('image')
    city_gallery3=CloudinaryField('image')
    city_gallery4=CloudinaryField('image')
    city_gallery5=CloudinaryField('image')
    city_map=CloudinaryField('image')
    
    def __str__(self):
        return self.city_name
    
class packages(models.Model):
    city = models.ForeignKey(Basecitypage, on_delete=models.CASCADE, related_name="packages",null=True, blank=True)
    package_image=CloudinaryField('image')
    package_name=models.CharField(max_length=50)
    discount_price=models.IntegerField()
    full_price=models.IntegerField()
    Availability=models.CharField(max_length=25,null=True, blank=True)
    no_of_days=models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.package_name} - {self.city.city_name}"
    
class Package_details(models.Model):
    package = models.OneToOneField(packages, on_delete=models.CASCADE, related_name="details",null=True, blank=True)
    cityheading=models.CharField(max_length=50)
    city_sub_desc=models.CharField(max_length=100)
    video1=CloudinaryField('video',resource_type='video')
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    region=models.CharField(max_length=200)
    temperature1=models.CharField(max_length=30)
    temperature2=models.CharField(max_length=30)
    eventcost=models.IntegerField()
    flashsaleprice=models.IntegerField()
    couplesharingcost=models.IntegerField()
    place1heading=models.CharField(max_length=100)
    place1description=models.TextField()
    place2heading=models.CharField(max_length=100)
    place2description=models.TextField()
    place3heading=models.CharField(max_length=100)
    place3description=models.TextField()
    place4heading=models.CharField(max_length=100)
    place4description=models.TextField()
    staysheading=models.CharField(max_length=200)
    staysdescription=models.TextField()
    totalcost=models.IntegerField()
    meetingpointcity=models.CharField(max_length=50)
    image1=CloudinaryField('image')
    image2=CloudinaryField('image')
    image3=CloudinaryField('image')
    image4=CloudinaryField('image')
    image5=CloudinaryField('image')
    image6=CloudinaryField('image',null=True,blank=True)
    
    def __str__(self):
        return f"Details of {self.package.package_name}"
    

class package_details_category(models.Model):
    day=models.CharField(max_length=100)
    package_id=models.ForeignKey(
        packages, 
        on_delete=models.CASCADE, 
        blank=False,
        null=True
    )
    def __str__(self):
        return self.day

    
class package_details_sub(models.Model):
    t1=models.TextField()
    t2=models.TextField()
    t3=models.TextField()
    t4=models.TextField()
    text=models.TextField()
    pid = models.ForeignKey(
        package_details_category, 
        on_delete=models.CASCADE, 
        blank=False,
        related_name='packagedetails'
    )

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField() 
    submitted_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # To track booking time
    package = models.ForeignKey(packages, on_delete=models.CASCADE,null=True,blank=True) 


class signinModel(models.Model):
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=45,null=True)