from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

urlpatterns = [
    path('', views.post_list, name='post_list'),
]