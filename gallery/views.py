from django.shortcuts import render


# Create your views here.
def gallery(request):
    """ Return gallery page """
    return render(request, 'gallery/gallery.html')
