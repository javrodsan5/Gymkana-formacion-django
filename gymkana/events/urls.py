from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('v2/allevents', views.eventos.as_view(), name='list_all_eventsV2'),
    path('v2/events/<int:pk>', views.detalle_eventoV2.as_view(), name='event_detailsV2'),
    path('v2/events/create', views.crear_eventoV2.as_view(), name='event_createV2'),
    path('v2/events/<int:pk>/update', views.actualizar_eventoV2.as_view(), name='event_updateV2'),
    path('v2/events/<int:pk>/delete', views.borrar_eventoV2.as_view(), name='event_deleteV2')]