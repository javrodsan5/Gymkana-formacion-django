from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import New

def index(request):
    latest_news_list = New.objects.order_by('-publish_date')[:4]
    context = {'latest_news_list': latest_news_list}
    return render(request, 'news/v1/index.html', context)

def detail(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    return render(request, 'news/v1/detail.html', {'new': new})

class IndexView(generic.ListView):
    template_name = 'news/v2/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """
        Return the last three published news (not including those set to be
        published in the future).
        """
        return New.objects.filter(
            publish_date__lte=timezone.now()
        ).order_by('-publish_date')[:4]

class DetailView(generic.DetailView):
    model = New
    template_name = 'news/v2/detail.html'

    def get_queryset(self):
        """
        Excludes any news that aren't published yet.
        """
        return New.objects.filter(publish_date__lte=timezone.now())

class CreateView(generic.edit.CreateView):
    model = New
    template_name = 'news/v2/create.html'
    fields = ['title', 'subtitle', 'body', 'image']

    def form_valid(self, form):
        if form.instance.image.format in ['JPG', 'PNG']:
            #somestuff
            return super().form_valid(form)
        else:
            raise TypeError()

    def get_success_url(self):
        return reverse('news:detail', kwargs={'pk': self.object.id})

class UpdateView(generic.edit.UpdateView):
    model = New
    template_name = 'news/v2/update.html'
    fields = ['title', 'subtitle', 'body', 'image']

    def get_success_url(self):
        return reverse('news:detail', kwargs={'pk': self.object.id})

class DeleteView(generic.edit.DeleteView):
    model = New

    #Saltar plantilla de confirmacion del delete
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('news:index')