from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator
def home(request):
    return render(request, 'Songs/index.html')


def artist(request):
    artists = KonkaniSongs.objects.values('artist').distinct()
    context = {
        'artists': artists
    }
    return render(request, 'Songs/artist.html', context)


# def album(request, name):
#     artistA = KonkaniSongs.objects.filter(artist=name).distinct()

#     print(name)
#     context = {
#         'artists': artistA
#     }
#     return render(request, 'Songs/albums.html', context)


def songs(request,name):
    print(name)
    songa = KonkaniSongs.objects.filter(artist=name)
    paginator=Paginator(songa,2)
    page=request.GET.get('page')
    paged_songs=paginator.get_page(page)
    context = {
        'songs': paged_songs
    }
    return render(request, 'Songs/songs.html', context)
