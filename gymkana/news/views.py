from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import New

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """
        Return the last three published news (not including those set to be
        published in the future).
        """
        return New.objects.filter(
            publish_date__lte=timezone.now()
        ).order_by('-publish_date')[:3]

class DetailView(generic.DetailView):
    model = New
    template_name = 'news/detail.html'

    def get_queryset(self):
        """
        Excludes any news that aren't published yet.
        """
        return New.objects.filter(publish_date__lte=timezone.now())