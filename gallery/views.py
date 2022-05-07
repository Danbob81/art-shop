""" A view to return the gallery template """
from django.shortcuts import render


def gallery(request):
    """ Return gallery page """
    return render(request, 'gallery/gallery.html')
