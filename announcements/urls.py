from django.urls import path
from .views import home, add_announcement

urlpatterns = [
    path('', home, name='home'),
    path('announcement/add/', add_announcement, name='add_announcement'),
]