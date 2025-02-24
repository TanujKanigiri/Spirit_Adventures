from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm

app_name='app1'

urlpatterns = [
    path('',home, name='home'),
    path('getintouch/',getintouch, name='getintouch'),
    path('city/<str:city_name>/', cityconnection, name='cityconnection'),
    path('package/<int:package_id>/', package_details, name='package_details'),
    path('contact/',contact,name='contact'),
    
    
    path('signup/',signupView,name='signup'),
    path('signin/',signinView,name='signin'),
    path('logout/',logoutView,name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='registration/password_reset_confirm.html',success_url='/reset/done/'
    # ), name='password_reset_confirm'),
    
    path(
        'reset/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]
