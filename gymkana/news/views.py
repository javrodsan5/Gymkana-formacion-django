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
    new = get_object_or_404(New, pk=new_id)
    form = NewForm(request.POST, request.FILES, instance=new)
    if form.is_valid():
        # if check_imagen(form.cleaned_data['image']):
        form.save()
        return HttpResponseRedirect('/news/v1/allnews')
    else:
        form = NewForm()

    return render(request, 'news/updateV1.html', {'form': form})


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
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            # img = form.cleaned_data['image']
            # if img:
            #     print("jpg" in img)
            #     print("png" in img)

            #     if ".png" in img or ".jpg" in img:
            form.save()
            # else:
            #     raise ValidationError("Debe ser png o jpg")
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
    fields = ['title', 'subtitle', 'body', 'image']
    success_url = "/news/v2/allnews"


class actualizar_noticiaV2(generic.UpdateView):

    model = New
    template_name = 'news/updateV2.html'
    fields = ['title', 'subtitle', 'body', 'image']
    success_url = "/news/v2/allnews"


class borrar_noticiaV2(generic.DeleteView):
    model = New
    success_url = "/news/v2/allnews"
