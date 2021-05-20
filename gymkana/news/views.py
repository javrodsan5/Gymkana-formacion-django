from events.models import Event
from django.shortcuts import get_object_or_404, render
from .models import New
from django.views import generic


def index(request):
    three_latest_news = New.objects.order_by('publish_date')[3:]
    #three_latest_events = Event.objects.order_by('-end_date')[:3]

    return render(request, 'news/index.html', {'three_latest_news': three_latest_news})


def noticiasV1(request):
    news = New.objects.all()

    return render(request, 'news/allnewsV1.html', {'news': news})


def detalle_noticiaV1(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    return render(request, 'news/detailsV1.html', {'new': new})

#--------------------------------------------------------------------------------

class noticiasV2(generic.ListView):
    template_name = 'news/allnewsV2.html'
    context_object_name = 'news'

    def get_queryset(self):
        return New.objects.all()


class detalle_noticiaV2(generic.DetailView):

    model = New
    template_name = 'news/detailsV2.html'
