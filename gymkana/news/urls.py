from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('v1/', views.index, name='index'),
    path('v1/<int:new_id>/', views.detail, name='detail'),
    path('v2/', views.IndexView.as_view(), name='index'),
    path('v2/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('v2/create/', views.CreateView.as_view(), name='create'),
    path('v2/update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('v2/delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]