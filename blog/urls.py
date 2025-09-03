from django.urls import path
from blog.views.post_view import HelloWorldView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='home'),
]