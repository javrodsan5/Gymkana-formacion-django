from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Event

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'next_events_list'

    def get_queryset(self):
        """
        Return the ongoing and next three events (not including those set to be
        ended in the past).
        """
        return Event.objects.filter(
            end_date__gte=timezone.now()
        ).order_by('start_date')[:3]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

    def get_queryset(self):
        """
        Excludes any events that aren't published yet.
        """
        return Event.objects.filter(start_date__gte=timezone.now())