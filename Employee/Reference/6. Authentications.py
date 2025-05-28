# Django’s authentication system provides a robust and extensible framework for managing user authentication and authorization. 
# It includes functionalities for handling user accounts, permissions, and access control.

# Here’s a comprehensive guide to understanding and implementing Django’s authentication system:

# 1. Key Components
# User Model: Represents user accounts.
# Authentication: Handles user login and logout.
# Authorization: Manages user permissions and access control.
# Password Management: Includes functionalities for password hashing, resetting, and changing.
# 2. Setup and Configuration
# 1. User Model
# Django comes with a built-in User model, but you can also create a custom user model if needed.

# Using the Built-In User Model:

from django.contrib.auth.models import User

# Custom User Model:

# Define a custom user model by extending AbstractUser or AbstractBaseUser.

"""
In Django, both `AbstractUser` and `AbstractBaseUser` are used for creating **custom user models**, 
but **you choose one based on how much customization you need**:

---

### ✅ Use `AbstractUser` if:

You want to **add extra fields** to Django's built-in `User` model but keep all default behavior like username, 
email, password, groups, permissions, etc.

#### Example:


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)


🟢 Pros:

* Easy to extend
* Keeps Django admin, authentication, and permissions working out of the box
* Recommended for **most use cases**

---

### ✅ Use `AbstractBaseUser` if:

You want **full control** over the user model — for example:

* Using **email instead of username** for login
* Removing unnecessary fields like `first_name`, `last_name`, `username`
* Creating a **totally different authentication system**

#### Example:


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()


🟢 Pros:

* Maximum flexibility (you define login field, behaviors, etc.)
* Good for **email-based login** or other non-standard auth

🔴 Cons:

* You must manually define everything (user manager, admin config, etc.)
* More work and more chance for bugs if not done properly

---

### 🚀 Summary:

| Use Case                              | Recommendation       |
| ------------------------------------- | -------------------- |
| Add custom fields to default user     | `AbstractUser` ✅     |
| Replace username with email login     | `AbstractBaseUser` ✅ |
| Fully custom user model               | `AbstractBaseUser` ✅ |
| Keep it simple, use default auth flow | `AbstractUser` ✅     |

"""


# Example:

# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    
# Update settings.py:


# settings.py
AUTH_USER_MODEL = 'myapp.CustomUser'

# 2. Authentication Views
# Django provides built-in views for user authentication.

# Login View:
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# Password Change and Reset Views:


from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Templates:

# Create templates for these views in your templates directory, e.g., registration/login.html, registration/password_reset_form.html.

# 3. User Authentication

# Login a User:


from django.contrib.auth import authenticate, login

def my_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect or return response
    else:
        pass
        # Handle failed login
        
# Logout a User:


from django.contrib.auth import logout

def my_logout_view(request):
    logout(request)
    # Redirect or return response
    
# 4. Authorization and Permissions
# Checking Permissions:

# You can use Django’s permission framework to check if a user has a specific permission.

# Example:


if request.user.has_perm('myapp.can_view'):
    pass
    # User has permission
# Assigning Permissions:

# Permissions can be assigned through Django’s admin interface or programmatically.

# Example:


from django.contrib.auth.models import Permission

permission = Permission.objects.get(codename='can_view')
user.user_permissions.add(permission)

# Custom Permissions:

# Define custom permissions in your model’s Meta class.

# Example:


# models.py
class MyModel(models.Model):
    ...

    class Meta:
        permissions = [
            ("can_view", "Can view this model"),
        ]
# Groups:

# Groups are a way to manage permissions for multiple users at once.

# Example:


from django.contrib.auth.models import Group

group = Group.objects.create(name='Editors')
group.permissions.add(permission)
user.groups.add(group)

# 5. Password Management
# Password Hashing:

# Django handles password hashing securely by default. You don’t need to manage password hashes manually.

# Changing Passwords:

# You can use the built-in views for password change and reset, as shown earlier.

# Password Reset:

# Django provides a full flow for password reset, including sending reset emails and confirming new passwords.

# Custom Password Validators:

# You can add custom password validators to enforce specific password policies.

# Example:


# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    ...
]

# 6. User Profiles
# You might need additional information beyond what the User model provides. Use a profile model linked to the user.

# Example:


# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
# Creating and Saving User Profiles:

# Use signals to automatically create and save profiles when a user is created.

# Example:

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
        
# Connect Signals:

# Ensure your signal handlers are connected, typically in apps.py:


# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals

# Summary:-

# User Model: Use Django’s built-in User model or create a custom one.
# Authentication Views: Use built-in views for login, logout, and password management.
# User Authentication: Use authenticate and login for logging users in, and logout for logging out.
# Authorization: Manage user permissions and groups, and check permissions using has_perm.
# Password Management: Handle password hashing, resetting, and validation.
# User Profiles: Extend user functionality with additional profile models and signals.
# By leveraging Django’s authentication system, you can implement a secure and flexible authentication and authorization framework for your application.
