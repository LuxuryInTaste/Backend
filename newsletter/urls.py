from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.newsletter_list, name='newsletter_list'),
]
