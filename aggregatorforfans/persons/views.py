from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .models import Person


def index(request):
    latest_persons_list = Person.objects.order_by('-id')[:5]
    context = {
        'latest_persons_list': latest_persons_list,
    }
    return render(request, 'persons/index.html', context)


def detail(request, person_id):
    return HttpResponse("Person id: %s." % person_id)
