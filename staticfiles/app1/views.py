from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from django.urls import reverse
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetView


# Create your views here.

def home(request):
    categories = category.objects.prefetch_related('subcategories').all()
    return render(request, 'home.html', {'categories': categories})


def getintouch(request):
    if request.method=='POST':
       l=userInfoForm(request.POST)
       if l.is_valid():
           l.save()
    st=userInfoForm()       
    return render(request, 'getintouch.html',{'data':st})


def cityconnection(request,city_name):
    city = get_object_or_404(Basecitypage, city_name__iexact=city_name)
    package =packages.objects.filter(city=city)
    f1 = feedbackForm()
    if request.method == 'POST':
        f1 = feedbackForm(request.POST)  
        if f1.is_valid():  
            f1.save()  
            return redirect('app1:cityconnection', city_name=city_name) 
    F=feedback.objects.all()  
    return render(request,'base_cities.html',{'city1':city,'packages':package,'form1':F})

# def cityconnection(request, city_name):
#     # Get the city and its packages
#     city = get_object_or_404(Basecitypage, city_name__iexact=city_name)
#     package = packages.objects.filter(city=city)

#     # Initialize the feedback form
#     f1 = feedbackForm()

#     # Handle form submission (Global Feedback)
#     if request.method == 'POST':
#         f1 = feedbackForm(request.POST)
#         if f1.is_valid():
#             f1.save()  # Save company-wide feedback
#             return redirect('app1:cityconnection', city_name=city_name)

#     # Fetch all company feedback (Global)
#     feedback_list = feedback.objects.all()

#     return render(request, 'base_cities.html', {
#         'city1': city,
#         'packages': package,
#         'form1': feedback_list,  # Global feedback
#         'f1': f1  # Feedback form
#     })



def package_details(request, package_id):
    package = get_object_or_404(packages, id=package_id)
    details = get_object_or_404(Package_details, package=package)  # Fetch package-specific details
    p_categories = package_details_category.objects.filter(package_id=package) \
        .prefetch_related('packagedetails')
    return render(request, 'package_details.html', {'package': package, 'details': details,'p_categories': p_categories})


# def signupView(request):
#     if request.method=='POST':  
#         s=signupform(request.POST)
#         if s.is_valid():
#             s.save()
#             return redirect('app1:signup')
#     return render(request,'signup.html',{'form':signupform()})

def signupView(request):
    r1=signupform()
    if request.method=='POST':
        r1=signupform(request.POST)
        if r1.is_valid():
            r1.save()
            username=r1.cleaned_data.get('username')
            password=r1.cleaned_data.get('password')
            email = r1.cleaned_data['email']
            user=authenticate(request,username=username,password=password,email=email)
            login(request, user)
            return redirect('app1:home')
    return render(request,'signup.html',{'form':r1})

# def signinView(request):
#     f1 = signinform()
#     if request.method == "POST":
#         form = signinform(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('app1:contact')
#             else:
#                 return render(request, 'signin.html', {'form': f1, 'error': 'Invalid username or password'})
#     return render(request, 'signin.html', {'form': f1})


def signinView(request):
    f1 = signinform()
    if request.method == "POST":
        form = signinform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Check if 'package' query parameter exists in the URL
                package_name = request.GET.get('package', None)
                if package_name:
                    # Redirect to 'contact' view with the package query parameter
                    return redirect(f'{reverse("app1:contact")}?package={package_name}')
                return redirect('app1:home')  # Default redirect if no package parameter
            else:
                return render(request, 'signin.html', {'form': f1, 'error': 'Invalid username or password'})
    return render(request, 'signin.html', {'form': f1})


def logoutView(request):
    logout(request)
    return redirect('app1:signin')



class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_done.txt'
    form_class=CustomPasswordResetForm

    def form_valid(self, form):
        form.save(
            request=self.request,
            use_https=self.request.is_secure(),
            email_template_name=self.email_template_name,
            subject_template_name=self.subject_template_name,
        )
        context = self.get_context_data(form=form)
        context['email_sent'] = True  
        return self.render_to_response(context)



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

    def form_valid(self, form):
        """
        When the form is valid, save the new password and render
        the same template with a success message.
        """
        form.save()
        context = self.get_context_data(form=form)
        context['reset_success'] = True  # Flag to indicate success
        return self.render_to_response(context)



from urllib.parse import unquote

def contact(request):
    package_name = request.GET.get('package', None)  # Get package name from URL
    
    if not package_name:
        return HttpResponse("Package not found", status=404)

    # Decode the URL-encoded package name (e.g., %20 to space, %26 to &)
    package_name = unquote(package_name).strip()

    # Log the decoded package name for debugging
    print(f"Decoded Package Name: {package_name}")

    # Try to find a package by name (case-insensitive and handles special characters)
    try:
        package = packages.objects.filter(package_name__icontains=package_name).first()
        if not package:
            raise packages.DoesNotExist
    except packages.DoesNotExist:
        print("Package not found in database")
        return HttpResponse("Package not found", status=404)

    # Debug: Confirm package match
    print(f"Matched Package: {package}")

    form = ContactForm()
    success_message = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package  # Associate the package with the booking
            booking.save()

            # Send confirmation email
            subject = f"Booking Confirmation - {package.package_name}"
            message = f"""
            Dear {booking.first_name},

            Your booking for the "{package.package_name}" package has been confirmed!

            Booking Details:
            - Name: {booking.first_name} {booking.last_name}
            - Email: {booking.email}
            - Phone: {booking.phone}
            - Address: {booking.address}
            - Package: {package.package_name}

            Thank you for choosing Spirit Adventures!
            We look forward to making your trip memorable.

            Best Regards,
            Spirit Adventures Team
            """

            send_mail(
                subject,
                message,
                "spiritadventures6@gmail.com",
                [booking.email, "spiritadventures6@gmail.com"],
                fail_silently=False,
            )

            success_message = "Your booking has been confirmed successfully!"

    return render(request, 'contactdetails.html', {'form': form, 'success_message': success_message, 'package': package})