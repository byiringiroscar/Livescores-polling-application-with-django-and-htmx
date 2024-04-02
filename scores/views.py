from django.shortcuts import render
from scores.models import Fixture

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def fixtures(request):
    fixtures = Fixture.objects.all()
    context = {
        'fixtures': fixtures

    }
    return render(request, 'fixtures.html', context)