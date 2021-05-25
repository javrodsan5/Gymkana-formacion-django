from django.shortcuts import render
from events.models import Event
from news.models import New


def index(request):
    three_latest_news = New.objects.order_by('-publish_date')[:3]
    three_latest_events = Event.objects.order_by('-end_date')[:3]

    return render(request, 'baseDjango/index.html', {'three_latest_news': three_latest_news, 'three_latest_events': three_latest_events})