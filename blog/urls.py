from django.urls import path
from .views import BlogLisView

app_name="blog"

urlpatterns = [
    path('', BlogLisView.as_view(), name="home")    
]
