from django.shortcuts import render
from scores.models import Fixture

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def fixtures(request):
    fixtures = Fixture.objects.all()


    # check if all are completed the game is FT
    all_completed = all(f.game_finished for f in fixtures)
    context = {
        'fixtures': fixtures,
        'all_completed': all_completed

    }
    if request.htmx:
        return render(request, 'partials/fixturelist.html', context)
    return render(request, 'fixtures.html', context)