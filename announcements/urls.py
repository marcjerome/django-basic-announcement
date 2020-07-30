from django.urls import path
from .views import home, add_announcement, delete_announcement, update_announcement

urlpatterns = [
    path('', home, name='home'),
    path('announcement/add/', add_announcement, name='add_announcement'),
    path('announcement/delete/<int:pk>/', delete_announcement, name='delete_announcement'),
    path('announcement/update/<int:pk>/', update_announcement, name='update_announcement'),
]