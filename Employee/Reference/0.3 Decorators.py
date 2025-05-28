# Django decorators are a powerful feature that allow you to modify or extend the behavior of view functions. 
# Decorators are often used to add functionality to views, such as authentication checks, permission checks, or logging.

### **1. Built-in Django Decorators**

# Django provides several built-in decorators that you can use to add functionality to your views.

#### **1.1 `@login_required`**

#Description**: Ensures that a user is authenticated before accessing a view. 
# If the user is not logged in, they are redirected to the login page.
#Usage**:

  
# myapp/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def my_view(request):
    return render(request, 'my_template.html')


# This decorator is useful for protecting views that should only be accessible to logged-in users.

#### **1.2 `@permission_required`**

#Description**: Ensures that a user has a specific permission before accessing a view.
#Usage**:

  
# myapp/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('myapp.can_edit', raise_exception=True)
def edit_view(request):
    return render(request, 'edit_template.html')
  

# Replace `'myapp.can_edit'` with the actual permission you want to check.

#### **1.3 `@staff_member_required`**

#Description**: Ensures that only staff members can access a view.
#Usage**:

  
# myapp/views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def staff_view(request):
    return render(request, 'staff_template.html')


# This decorator is useful for views that should only be accessible to staff members.

### **2. Custom Decorators**

# You can also create your own decorators to add custom behavior to your views.

#### **2.1 Creating a Simple Decorator**

# A decorator is a function that takes another function as an argument and returns a new function that usually extends the behavior of the original function.

#Example**:

  
# myapp/decorators.py
from django.http import HttpResponseForbidden

def custom_decorator(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You are not authorized to view this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


# This decorator checks if the user is authenticated and returns a forbidden response if they are not.

#### **2.2 Using the Custom Decorator**

#Example**:

  
# myapp/views.py
from django.shortcuts import render
from .decorators import custom_decorator

@custom_decorator
def protected_view(request):
    return render(request, 'protected_template.html')
  

### **3. Decorators with Arguments**

# Some decorators need to accept arguments to provide more flexible functionality.

#### **3.1 Example of a Decorator with Arguments**

#Example**:

  
# myapp/decorators.py
from django.http import HttpResponseForbidden

def user_required(user_type):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or not getattr(request.user, 'user_type', None) == user_type:
                return HttpResponseForbidden("You are not authorized to view this page.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
  

# This decorator checks if the user is authenticated and whether their `user_type` matches the required type.

#### **3.2 Using the Decorator with Arguments**

#Example**:

# myapp/views.py
from django.shortcuts import render
from .decorators import user_required

@user_required('admin')
def admin_view(request):
    return render(request, 'admin_template.html')
  

### **4. Stacked Decorators**

# You can apply multiple decorators to a single view function. Decorators are applied from bottom to top.

#### **4.1 Example of Stacked Decorators**

#Example**:
  
# myapp/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@login_required
@permission_required('myapp.can_edit', raise_exception=True)
def edit_view(request):
    return render(request, 'edit_template.html')