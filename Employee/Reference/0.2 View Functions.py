"""
In Django, view functions are the core components responsible for handling HTTP requests 
and returning HTTP responses. They are defined in the `views.py` file of your Django application. 
Each view function processes a request, interacts with models, and renders a response (usually a web page or JSON data).
"""

# Here’s a detailed overview of Django view functions, including their creation, types, and usage:

### #1. Basic View Functions#

# A basic view function takes an HTTP request as input and returns an HTTP response. 

#### #1.1 Creating a Simple View Function#

#Example#:

  
# myapp/views.py
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


# This function responds to HTTP requests with a plain text message.

#### #1.2 Mapping View Functions to URLs#

# You map view functions to URL patterns in the `urls.py` file.

#Example#:

  
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
  

### #2. Handling Templates#

# View functions often render HTML templates to generate dynamic web pages.

#### #2.1 Rendering Templates#

# Use the `render` shortcut to render templates.

#Example#:

  
# myapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'message': 'Hello, world!'})


# This function renders the `index.html` template and passes a context dictionary to it.

#### #2.2 Template Example#

#index.html#:

# html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Index</title>
# </head>
# <body>
#     <h1>{{ message }}</h1>
# </body>
# </html>
  

### #3. Handling Forms#

# View functions can process form submissions by handling `POST` requests.

#### #3.1 Processing Forms#

#Example#:

  
# myapp/forms.py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

# myapp/views.py
from django.shortcuts import render
from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'name_form.html', {'form': form})
  

# This function handles form submission and validation.

#### #3.2 Form Template Example#

#name_form.html#:

# html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Name Form</title>
# </head>
# <body>
#     <form method="post">
#         {% csrf_token %}
#         {{ form.as_p }}
#         <button type="submit">Submit</button>
#     </form>
# </body>
# </html>


### #4. Class-Based Views#

# Django also supports class-based views (CBVs), which provide more structure and reuse functionality for views.

#### #4.1 Using Class-Based Views#

#Example#:

  
# myapp/views.py
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the index.")
  

#### #4.2 Mapping Class-Based Views to URLs#

#Example#:
  
# myapp/urls.py
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
  

### #5. Using Django’s Generic Views#

# Django provides built-in generic views for common patterns like displaying lists and detail views.

#### #5.1 ListView Example#

#Example#:

  
# myapp/views.py
from django.views.generic import ListView
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
  

#### #5.2 DetailView Example#

#Example#:

  
# myapp/views.py
from django.views.generic import DetailView
from .models import Item

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'


#### #5.3 Mapping Generic Views to URLs#

#Example#:

  
# myapp/urls.py
from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]
  

### #6. Handling HTTP Methods#

# View functions can handle different HTTP methods like GET, POST, PUT, DELETE.

#### #6.1 Handling Multiple Methods#

#Example#:

  
# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def api_view(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'GET request'})
    elif request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'message': 'POST request', 'data': data})
      
#########################################################################################

# In your Django view:


@csrf_exempt
def api_view(request):
    ...


# You're using `@csrf_exempt` to **disable CSRF protection** for this particular view. Here's why and when it's used:



### 🔒 What is CSRF?

# **CSRF** (Cross-Site Request Forgery) is a security mechanism to **prevent unauthorized POST requests** 
# from malicious sites on behalf of a logged-in user.

# * Django includes CSRF protection by default on views that modify data (POST, PUT, DELETE).
# * It requires a **CSRF token** to be included in the request (usually as a hidden form field or header).

### 🚫 Why use `@csrf_exempt`?

# You use `@csrf_exempt` when:

# * You're building an **API endpoint** (like a mobile app or third-party service) that does **not use Django's CSRF token system**.
# * You want to **allow unauthenticated or public POST requests** without CSRF validation.

# **In your code:**


@csrf_exempt
def api_view(request):
  pass


# This is necessary because you're accepting JSON POST data from clients 
# (e.g., fetch, Postman, mobile apps), and those won't include Django's CSRF token by default.



### ⚠️ Warning: Don't overuse it

# * Using `@csrf_exempt` **lowers security**, so **only use it when absolutely necessary** (like for APIs).
# * For APIs, it's safer to use:

# * Django REST Framework (DRF), which handles this securely.
# * Token-based authentication (e.g., JWT) instead of relying on CSRF.



### ✅ Best practice for APIs:

# If you're building APIs:

# * Use Django REST Framework (DRF)
# * Use `@api_view` or APIView classes
# * Use proper auth (e.g., Token, JWT)
# * Skip CSRF **only where safe and appropriate**

###############################################################################################################


### #7. Error Handling#

# You can handle errors in views and return custom error pages.

#### #7.1 Custom Error Handling#

#Example#:


# myapp/views.py
# from django.http import HttpResponseNotFound

# def page_not_found(request, exception):
#   return HttpResponseNotFound("Custom 404 Page Not Found")

# You’ll need to configure this in your `urls.py` file:


# myproject/urls.py
# handler404 = 'myapp.views.page_not_found