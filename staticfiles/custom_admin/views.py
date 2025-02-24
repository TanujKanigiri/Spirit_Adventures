from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from app1.models import category, sub_category, packages, Basecitypage,Contact
from .forms import CategoryForm, SubcategoryForm, PackagesForm


#Custom Admin Login

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "admin123":
            request.session["admin_logged_in"] = True  # Set session
            return redirect("custom_admin:booking_details")  # Redirect to Booking Details after login
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "custom_admin/admin.html")

#Custom Admin Logout

def custom_logout(request):
    request.session.flush()  
    return redirect("custom_admin:login") 


#Booking Details (Only for Admin)

def booking_details(request):
    if not request.session.get("admin_logged_in"):
        return redirect("custom_admin:login") 
    bookings = Contact.objects.all().order_by('-submitted_at')  
    return render(request, "custom_admin/bookingdetails.html", {"bookings": bookings})


#Category CRUD

def category_list(request):
    if not request.session.get("admin_logged_in"):
        return redirect("custom_admin:custom_admin_login")
    categories = category.objects.all()  # Fetch categories
    print("Categories:", categories)  # Debugging: Check if data exists
    return render(request, "custom_admin/category_list.html", {"categories": categories})

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("custom_admin:category_list")
    else:
        form = CategoryForm()
    return render(request, "custom_admin/category_form.html", {"form": form})

def update_category(request, id):
    categori = get_object_or_404(category, id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=categori)
        if form.is_valid():
            form.save()
            return redirect("custom_admin:category_list")
    else:
        form = CategoryForm(instance=categori)
    return render(request, "custom_admin/category_form.html", {"form": form})

def delete_category(request, id):
    category_obj = get_object_or_404(category, id=id)
    if request.method == "POST":
        category_obj.delete()
        return redirect("custom_admin:category_list")
    return render(request, "custom_admin/delete_confirm.html", {"object": category_obj})


#City CRUD

def city_list(request):
    if not request.session.get("admin_logged_in"):
        return redirect("custom_admin:custom_admin_login")

    cities = sub_category.objects.all().select_related("cid")  # Use 'cid' instead of 'category'
    print("Cities:", cities)  # Debugging

    return render(request, "custom_admin/city_list.html", {"cities": cities})

def create_city(request):
    if not request.session.get("admin_logged_in"):
        return redirect("custom_admin:custom_admin_login")

    categories = category.objects.all()  # Fetch categories for dropdown

    if request.method == "POST":
        name = request.POST.get("name")
        category_id = request.POST.get("category")  # Should match <select> name in form

        if name and category_id:  # Ensure both fields are filled
            category_instance = category.objects.get(id=category_id)  # Fetch category instance
            new_city = sub_category(name=name, cid=category_instance)  # Correct ForeignKey usage
            new_city.save()
            return redirect("custom_admin:city_list")  # Redirect to cities list after adding

    return render(request, "custom_admin/city_form.html", {"categories": categories})

def update_city(request, id):
    categories = category.objects.all()  # Fetch categories
    city = get_object_or_404(sub_category, id=id)
    if request.method == "POST":
        form = SubcategoryForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect("custom_admin:city_list")
    else:
        form = SubcategoryForm(instance=city)
    return render(request, "custom_admin/city_form.html", {"form": form, "categories": categories, "city": city})

def delete_city(request, id):
    city = get_object_or_404(sub_category, id=id)
    if request.method == "POST":
        city.delete()
        return redirect("custom_admin:city_list")
    return render(request, "custom_admin/delete_confirm.html", {"object": city})


#Package CRUD

def package_list(request):
    if not request.session.get("admin_logged_in"):
        return redirect("custom_admin:custom_admin_login")
    packages_list = packages.objects.all().select_related("city")  
    return render(request, "custom_admin/package_list.html", {"packages": packages_list})

def create_package(request):
    if not request.session.get("admin_logged_in"):
        return redirect("custom_admin:custom_admin_login")
    cities = Basecitypage.objects.all()
    if request.method == "POST":
        form = PackagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("custom_admin:package_list")
        else:
            print(form.errors)
    else:
        form = PackagesForm()
    return render(request, "custom_admin/package_form.html", {"form": form, "cities": cities})

def update_package(request, id):
    cities = sub_category.objects.all()  # Fetch cities
    package = get_object_or_404(packages, id=id)
    if request.method == "POST":
        form = PackagesForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect("custom_admin:package_list")
    else:
        form = PackagesForm(instance=package)
    return render(request, "custom_admin/package_form.html", {"form": form, "cities": cities, "package": package})

def delete_package(request, id):
    package = get_object_or_404(packages, id=id)
    if request.method == "POST":
        package.delete()
        return redirect("custom_admin:package_list")
    return render(request, "custom_admin/delete_confirm.html", {"object": package})