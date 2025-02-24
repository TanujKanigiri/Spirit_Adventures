from django.urls import path
from .views import *

app_name='custom_admin'

urlpatterns = [
    path('custom-admin/login/', custom_login, name='login'), 
    path('custom-admin/logout/', custom_logout, name='logout'),
    path('custom-admin/bookingdetails/', booking_details, name='booking_details'),

    # CRUD Operations
    path("categories/", category_list, name="category_list"),
    path("categories/add/", create_category, name="create_category"),
    path("categories/edit/<int:id>/", update_category, name="update_category"),
    path("categories/delete/<int:id>/", delete_category, name="delete_category"),

    path("cities/", city_list, name="city_list"),
    path("cities/add/", create_city, name="create_city"),
    path("cities/edit/<int:id>/", update_city, name="update_city"),
    path("cities/delete/<int:id>/", delete_city, name="delete_city"),

    path("packages/", package_list, name="package_list"),
    path("packages/add/", create_package, name="create_package"),
    path("packages/edit/<int:id>/", update_package, name="update_package"),
    path("packages/delete/<int:id>/", delete_package, name="delete_package"),
]
