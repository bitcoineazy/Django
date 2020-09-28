from . import views as homepage_views
from django.urls import path, include


urlpatterns = [
    path('', homepage_views.homepage)
]