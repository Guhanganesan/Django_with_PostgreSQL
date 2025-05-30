# Django’s caching framework is a powerful tool for improving the performance of your application by storing and reusing expensive or frequently accessed data. 
# Caching can help reduce database queries, speed up page loads, and improve overall efficiency.

# Overview of Django Caching
# Django supports various caching backends and strategies. The most common types of caching are:

# Database Caching: Caches data in the database.
# File-Based Caching: Stores cached data in files on the filesystem.
# Memory-Based Caching: Uses in-memory storage, such as with locmem or memcached.
# Distributed Caching: Uses systems like Redis or memcached for caching across multiple servers.
# Configuring Caching
# You can configure caching in Django by setting up the CACHES setting in your settings.py file. 
# Here’s an overview of different caching backends:

# 1. In-Memory Caching
# The simplest caching backend, suitable for development and small-scale deployments.


# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# 2. File-Based Caching
# Stores cached data in files on the server’s filesystem.


# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/path/to/cache/directory',
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# 3. Memcached

# A distributed memory caching system. Django supports both python-memcached and pylibmc.

# Using pylibmc:


# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Using python-memcached:

# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# 4. Redis
# Redis is a popular, fast, and flexible caching backend.

# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# Using Caching
# 1. Caching with the Cache API
# Django provides a caching API for setting, retrieving, and deleting cache data.

# Setting Cache Data:

from django.core.cache import cache

# Set a cache value with a timeout of 60 seconds
cache.set('my_key', 'my_value', timeout=60)

# Getting Cache Data:

# Retrieve the cache value
value = cache.get('my_key')

# Delete a specific cache key
cache.delete('my_key')

# Delete all cache keys
cache.clear()


# 2. Caching Views
# You can cache entire views or parts of views to improve performance.

# Using cache_page Decorator:

# The cache_page decorator caches the output of a view for a specified period.


from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache the view for 15 minutes
def my_view(request):
    # Expensive operations
    return render(request, 'my_template.html', {})

# Using cache in Templates:

# You can cache parts of templates with the {% cache %} template tag.

# html
# Copy code
# {% load cache %}
# {% cache 600 my_template_cache_key %}
#     <!-- Content to cache -->
# {% endcache %}
# 3. Template Fragment Caching
# Cache specific fragments of a template to avoid regenerating them on every request.

# Example:

# html
# Copy code
# {% load cache %}
# {% cache 600 my_fragment_cache_key %}
#     <!-- Fragment to cache -->
# {% endcache %}
# 4. Per-View Cache
# Use Django’s cache framework to cache the output of individual views programmatically.

# Example:


from django.core.cache import cache
from django.shortcuts import render

def my_view(request):
    cache_key = 'my_view_cache_key'
    response = cache.get(cache_key)

    if not response:
        response = render(request, 'my_template.html', {})
        cache.set(cache_key, response, timeout=60*15)
    
    return response

# Best Practices
# Cache Invalidations: Ensure that your cache invalidates or updates correctly when the underlying data changes.
# Cache Size: Monitor and manage cache size to avoid using excessive memory or storage.
# Security: Avoid caching sensitive data and ensure that your caching setup is secure.
# Testing: Test caching configurations thoroughly in your development and staging environments to ensure they work as expected.

# Summary:-

# Caching Backends: Django supports various caching backends like in-memory, file-based, Memcached, and Redis.
# Cache API: Use Django’s cache API to set, get, and delete cache data.
# View Caching: Cache entire views using decorators or cache_page.
# Template Caching: Cache parts of templates using {% cache %} and template fragment caching.
# Best Practices: Manage cache size, invalidate caches appropriately, and ensure security.
# By utilizing Django’s caching framework, you can significantly enhance the performance of your application and improve user experience.