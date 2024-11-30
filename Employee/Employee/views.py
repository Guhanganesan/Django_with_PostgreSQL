from rest_framework.authtoken.models import Token
from django.http import HttpResponse

def verify_token(request):
    token = Token.objects.get(key='b953dd65ca5d05717b8fd195c34fad58aeca1545')
    print(token.user)
    return HttpResponse(token.user)