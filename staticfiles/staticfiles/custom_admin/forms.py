from django import forms  
from app1.models import category, sub_category, packages,Basecitypage  

class CategoryForm(forms.ModelForm):  
    class Meta:  
        model = category  
        fields = '__all__'  

class SubcategoryForm(forms.ModelForm):  
    category = forms.ModelChoiceField(queryset=category.objects.all(), empty_label="Select Category")  

    class Meta:  
        model = sub_category  
        fields = '__all__' 

class PackagesForm(forms.ModelForm):  
    city = forms.ModelChoiceField(queryset=Basecitypage.objects.all(), empty_label="Select City")  

    class Meta:  
        model = packages  
        fields = '__all__'

