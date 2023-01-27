from django.urls import path
from .views import BlogLisView, BlogCreateView

app_name="blog"

urlpatterns = [
    path('', BlogLisView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create")    
]

