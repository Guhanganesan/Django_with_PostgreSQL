from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.shortcuts import redirect

# Create your views here.

def http_response(request):
    return HttpResponse("Hello, World!")

def my_json_view(request):
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)

def my_template_view(request):
    context = {'name': 'Guhan Ganesan'}
    return render(request, 'my_template.html', context)

def my_redirect_view(request):
    return redirect('https://github.com/Guhanganesan/Django_with_PostgreSQL')


def stream_view(request):
    def stream_generator():
        for i in range(1, 6):
            yield f"Chunk {i}\n"
    return StreamingHttpResponse(stream_generator(), content_type='text/plain')

def custom_header_view(request):
    response = HttpResponse("Custom Header Response")
    response['Custom-Header'] = 'MyValue'
    return response
