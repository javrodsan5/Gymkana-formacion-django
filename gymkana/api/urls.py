from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('events/', views.event_list),
    path('events/<int:pk>/', views.event_detail),
]
