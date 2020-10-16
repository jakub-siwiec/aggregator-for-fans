from django.views import generic

# Create your views here.

from .models import Person


class IndexView(generic.ListView):
    paginate_by = 2
    template_name = 'persons/index.html'
    context_object_name = 'latest_persons_list'

    def get_queryset(self):
        return Person.objects.order_by('-id')[:5]


class DetailView(generic.DetailView):
    model = Person
    template_name = 'persons/detail.html'
