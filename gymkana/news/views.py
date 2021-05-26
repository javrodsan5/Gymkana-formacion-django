from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from .models import New
from django.views import generic
from PIL import Image
from .forms import NewForm
from django.http import HttpResponseRedirect


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


def editar_noticiaV1(request, new_id):
    # import ipdb
    # ipdb.set_trace()
    new = get_object_or_404(New, pk=new_id)
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/news/v1/allnews")
    else:
        data = {'title': new.title, 'subtitle': new.subtitle,
                'body': new.body, 'image': new.image}
        form = NewForm(data, request.POST, request.FILES, instance=new)

    return render(request, 'news/updateV1.html', {'form': form})


def createV1(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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


class crear_noticiaV2(generic.CreateView):

    model = New
    template_name = 'news/createV2.html'
    form_class = NewForm
    success_url = "/news/v2/allnews"


class actualizar_noticiaV2(generic.UpdateView):

    model = New
    template_name = 'news/updateV2.html'
    form_class = NewForm
    success_url = "/news/v2/allnews"


class borrar_noticiaV2(generic.DeleteView):
    model = New
    success_url = "/news/v2/allnews"
