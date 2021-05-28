from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('events/', views.EventList.as_view(),  name='listApi'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='detailsApi'),
]
