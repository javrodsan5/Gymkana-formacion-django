from django.core.exceptions import ValidationError
from events.models import Event
from django.shortcuts import get_object_or_404, render
from .models import New
from django.views import generic
from PIL import Image
from .forms import NewForm
from django.http import HttpResponseRedirect
from django.utils import timezone


def index(request):
    three_latest_news = New.objects.order_by('-publish_date')[:3]
    three_latest_events = Event.objects.order_by('-end_date')[:3]

    return render(request, 'news/index.html', {'three_latest_news': three_latest_news, 'three_latest_events': three_latest_events})


def noticiasV1(request):
    news = New.objects.all()

    return render(request, 'news/allnewsV1.html', {'news': news})


def detalle_noticiaV1(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    return render(request, 'news/detailsV1.html', {'new': new})


def borrar_noticiaV1(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    new.delete()
    return HttpResponseRedirect('/news/v1/allnews')


def check_imagen(image):
    if image._size < 10485760:
        img = Image.open(image)
        img.verify()
        if img.format in ('png', 'jpg'):
            return True
        else:
            raise ValidationError(
                "Unsupported image type. Please upload jpg or png")
    else:
        raise ValidationError("The image size must be under 10MB")


def createV1(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            new = New()
            new.title = form.cleaned_data['title']
            new.subtitle = form.cleaned_data['subtitle']
            new.body = form.cleaned_data['body']
            #new.image = request.POST['iamge']
            new.save()
            return HttpResponseRedirect('/news/v1/allnews')
    else:
        form = NewForm()

    return render(request, 'news/createV1.html', {'form': form})

# --------------------------------V2------------------------------------------------


class noticiasV2(generic.ListView):
    template_name = 'news/allnewsV2.html'
    context_object_name = 'news'

    def get_queryset(self):
        return New.objects.all()


class detalle_noticiaV2(generic.DetailView):

    model = New
    template_name = 'news/detailsV2.html'
