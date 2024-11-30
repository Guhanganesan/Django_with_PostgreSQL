from .viewsets import Userviewsets
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('users', Userviewsets, basename='user')