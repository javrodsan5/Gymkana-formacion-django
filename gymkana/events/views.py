from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from .models import Event
from django.views import generic
from PIL import Image
from django.http import HttpResponseRedirect

class eventos(generic.ListView):
    template_name = 'events/alleventsV2.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all()


class detalle_eventoV2(generic.DetailView):

    model = Event
    template_name = 'events/detailsV2.html'


class crear_eventoV2(generic.CreateView):

    model = Event
    template_name = 'events/create_eventV2.html'
    fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']
    success_url = "/events/v2/allevents"


class actualizar_eventoV2(generic.UpdateView):

    model = Event
    template_name = 'events/updateV2.html'
    fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']
    success_url = "/events/v2/allevents"

class borrar_eventoV2(generic.DeleteView):
    model = Event
    success_url = "/events/v2/allevents"

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
