from django.urls import path
from . import views

urlpatterns = [
    path("/http_response",views.http_response, name='http_response'), # http://127.0.0.1:8000/tutorial/http_response
    path("/my_json_view",views.my_json_view, name='my_json_view'),
    path("/my_template_view", views.my_template_view, name='my_template_view'),
    path("/my_redirect_view", views.my_redirect_view, name='my_redirect_view'),
    path("/stream_view", views.stream_view, name='stream_view'),
    path("/custom_header_view",views.custom_header_view,name='custom_header_view')
]