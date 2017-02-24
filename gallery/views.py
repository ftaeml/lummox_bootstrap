from django.shortcuts import render
from .models import Limn, Album
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def carusel():
    images = Limn.objects.filter(ty_pe_id=4)
    return {"images": images}


def albums(request, id=None):
    paint = Album.objects.filter(type_id=id)
    paginator = Paginator(paint, 3)
    page = request.GET.get('page')

    try:
        paint = paginator.page(page)
    except PageNotAnInteger:
        paint = paginator.page(1)
    except EmptyPage:
        paint = paginator.page(paginator.num_pages)
    context = {"paints": paint, "pn":page}
    context.update(carusel())
    return render(request, "gallery/albums.html", context)


def gallery(request):
    images = Limn.objects.filter(ty_pe_id=4)
    context = {"images": images}
    return render(request, "gallery/index.html", context)


def album(request, id=None):
    title_album = Album.objects.filter(id=id)
    images = Limn.objects.filter(album_id=id)
    context = {"images":images, "title_album":title_album}
    return render(request, "gallery/photos.html", context)