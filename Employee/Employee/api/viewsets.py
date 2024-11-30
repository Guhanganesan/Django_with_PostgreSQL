from rest_framework import viewsets
from .serializers import userSerializers
from django.contrib.auth.models import User
 
 
class Userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all() # /api/users/
    serializer_class = userSerializers