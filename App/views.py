from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from . models import Category, Varieties, Disease,CropCategory
from . models import Symptom, Control
from . models import ProductCategory, CropVarieties, ProductVarieties 
from django . http import JsonResponse
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
User = get_user_model()


# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        if User.objects.filter(username= username).exists():
            messages.error(request, "Username has already been used")
            return redirect('signup')
        email = request.POST.get('email')
        if User.objects.filter(email= email).exists():
            messages.error(request, "Email has already been used")
            return redirect('signup')
        password = request.POST.get('password')
        
        if not lastname or not firstname or not username or not email or not password:
            print("Incomplete details")
        else:
            new_user = User.objects.create(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            new_user.set_password(password)
            new_user.save()
            return redirect('login')
        
        # Send a welcome email to the new user
        subject = 'Welcome to Your Website'
        from_email = 'horlharmighty2000@gmail.com'  # Replace with your email
        recipient_list = [email]
        
        # Load the email template with context data
        context = {'firstname': firstname}  # You can pass context data to your email template
        html_message = render_to_string('email/welcome.html', context)
        plain_message = strip_tags(html_message)  # Convert HTML to plain text for the email body
        
        # Send the email
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
        
    return render(request, 'html/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, 'Email or password is empty')
            return redirect('/login')
        
        user = auth.authenticate(username=email, password=password)
        if user is None:
            messages.error(request, 'Invalid login credentials')
            return redirect('/login')
        
        auth.login(request, user)
        return redirect('home')
    
    return render(request, 'html/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render (request, 'html/about.html')

def service(request):
    return render(request, 'html/services.html')

@login_required
def home(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'html/home.html', context)

@login_required
def market(request):
    category = ProductCategory.objects.all()
    context = {
        'category': category
    }
    
    return render(request, 'html/market.html', context)

@login_required
def varieties(request, id):
    cat = Category.objects.get(id = id)
    category = Varieties.objects.filter(category = cat)
    context = {"category": category, "name":cat.name }
    return render (request, 'html/varieties.html', context)

@login_required
def read(request, id):
    variety = Varieties.objects.get(id=id)
    diseases = variety.disease_set.all()
    symptoms = []
    controls = []
    for disease in diseases:
        disease_symptoms = disease.symptom_set.all()
        symptoms.extend(disease_symptoms)
        disease_controls = disease.control_set.all()
        controls.extend(disease_controls)
    context = {'variety': variety,
        'diseases': diseases,
        'symptoms': symptoms,
        'controls': controls,}
    return render (request, 'html/read.html', context)

@login_required
def crop(request):
    category = CropCategory.objects.all()
    context = {
        'category': category
    }
    return render(request, 'html/crop.html', context)

@login_required
def crops(request, id):
    cat = CropCategory.objects.get(id = id)
    category = CropVarieties.objects.filter(category = cat)
    context = {"category": category, "name":cat.name }
    return render (request, 'html/cropvarieties.html', context)

@login_required
def readcrops(request, id):
    variety = CropVarieties.objects.get(id=id)
    # diseases = Disease.objects.filter(varieties = variety)
    context = {"variety": variety}
    return render (request, 'html/readcrops.html', context)

@login_required
def products(request, id):
    cat = ProductCategory.objects.get(id = id)
    category = ProductVarieties.objects.filter(category = cat)
    context = {"category": category, "name":cat.name }
    return render (request, 'html/productvarieties.html', context)

@login_required
def readproduct(request, id):
    variety = ProductVarieties.objects.get(id=id)
    context = {"variety": variety}
    return render (request, 'html/readproduct.html', context)

@login_required
def cart (request):
    # customer = request.user.customer
    # order, created = order.objects.get_or_create(customer=customer, complete=False)
    return render(request, 'html/cart.html')


@login_required
def checkout (request):
    return render(request, 'html/checkout.html')

@login_required
def payment (request):
    return render(request, 'html/payment.html')

# def updateItems (request):
#     data = json.loads(request.data)
#     productId = ['productId']
#     action = data ['action']

#     print('action:', action)
#     print('productId', productId)

#     customer = request.user.customer
#     product = products.objects.get(id=productId)

#     order, created = order.objects.get_or_create(customer=customer, complete=False)
#     orderItem = orderItem.objects.get_or_created(order=order, product=product)

#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity +1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity -1)

#     orderItem.save()

#     if orderItem.quantity <= 0:
#         orderItem.delete()
#     return JsonResponse ('Item was added', safe=False)
