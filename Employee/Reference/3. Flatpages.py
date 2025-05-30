# Django Flatpages is a lightweight, built-in app provided by Django that allows you to manage simple, 
# static pages of content within your Django project. It is useful for adding and managing static pages
# such as "About Us", "Contact", "Terms of Service", etc., without requiring a full-fledged CMS.

# Here’s a guide to setting up and using Django Flatpages:

# 1. Install and Set Up Flatpages
# Add Flatpages to Installed Apps

# First, you need to ensure that django.contrib.sites and django.contrib.flatpages are added to your INSTALLED_APPS in settings.py.

# settings.py
INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.flatpages',
]

SITE_ID = 1

# Add Middleware

# Make sure the FlatpageMiddleware is included in your MIDDLEWARE settings to serve flatpages.


# settings.py
MIDDLEWARE = [
    'django.middleware.flatpages.FlatpageMiddleware',
]
# Run Migrations

# Run the migrations to set up the necessary database tables for flatpages.

# bash
# Copy code
# python manage.py migrate
# 2. Create Flatpages
# Use the Admin Interface

# Log in to the Django admin interface: Go to /admin and log in with your admin credentials.
# Navigate to Flatpages: Find the "Flatpages" section under the "Flatpages" app.
# Add a New Flatpage: Click "Add" to create a new flatpage. Fill in the following fields:
# URL: The URL path where the flatpage will be accessible. For example, /about/.
# Title: The title of the flatpage.
# Content: The content of the flatpage. This can be HTML.
# Enable or Disable: Choose whether the page is active or not.
# Create Flatpages Programmatically

# You can also create flatpages via the Django shell or a script.

# python
# Copy code
from django.contrib.flatpages.models import FlatPage

flatpage = FlatPage.objects.create(
    url='/about/',
    title='About Us',
    content='<h1>About Us</h1><p>This is the about us page.</p>',
    registration_required=False
)
# 3. Configure URL Patterns
# Add a URL pattern for serving flatpages. You can do this by including the flatpages.urls in your project’s URL configuration.


# urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
]

# 4. Customizing Flatpage Templates
# You may want to customize how flatpages are rendered. To do this, create a template that matches the flatpage’s template_name:

# Create a Template

# Create a template named flatpages/default.html in your templates directory.

# html
# Copy code
# <!-- templates/flatpages/default.html -->
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{% block title %}{{ flatpage.title }}{% endblock %}</title>
# </head>
# <body>
#     <h1>{{ flatpage.title }}</h1>
#     <div>
#         {{ flatpage.content|safe }}
#     </div>
# </body>
# </html>


# flatpage = FlatPage.objects.create(
#     url='/contact/',
#     title='Contact Us',
#     content='<h1>Contact Us</h1><p>This is the contact page.</p>',
#     template_name='flatpages/contact.html',
#     registration_required=False
# )

# 5. Apply Flatpages Permissions
# You can control access to flatpages using the registration_required field. If True, users must be logged in to view the page.

# 6. Admin Management
# The Flatpages admin interface allows you to:

# View and Edit Existing Flatpages: Manage flatpages through the admin interface.
# Search and Filter Flatpages: Find specific flatpages by title or URL.
# Summary
# Django Flatpages provide a simple way to manage static content within your Django project. Here's a recap of what you need to do:

# Set Up: Ensure django.contrib.sites and django.contrib.flatpages are in INSTALLED_APPS, add FlatpageMiddleware, and run migrations.
# Create and Manage: Use the admin interface or Django shell to create and manage flatpages.
# Configure URLs: Add a URL pattern for flatpages in your urls.py.
# Customize Templates: Create and use custom templates for rendering flatpages.
# Manage Access: Control access using the registration_required field.
# By following these steps, you can effectively use Django Flatpages to handle static content on your website.