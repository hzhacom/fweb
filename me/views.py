from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from .models import Note

# Create your views here.

def index(request):
    return render(request, 'me/index.html')

def error(request):
    raise Http404("Page not found")

class NoteView(ListView):
    paginate_by = 5
    model = Note
    template_name = 'me/mynote.html'
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.paginate_by
        obj = Note.objects.all()
        num_obj = len(obj)
        context['num_page'] = num_obj / self.paginate_by
        return context

def debug(request):
    return render(request, 'me/1.html')