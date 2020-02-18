from django.shortcuts import render
from fotogram.models import Profile, Album, Photo, Tag
from fotogram.forms import CustomerForm, AlbumAddForm, PhotographerForm, AlbumAddPhotoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# from demo_form.forms import *
# from demo_form.models import Author, Book
from django.urls import reverse


def profilecomplete(request):
    if request.method == 'POST':
        data = Profile.objects.get(user=request.user)
        form = CustomerForm(request.POST, request.FILES, instance=data)
        form.save()
        if request.user.profile.is_photographer():
            return HttpResponseRedirect(reverse('profile'))

    if request.user.profile.is_customer():
        form = CustomerForm()
        return render(request, 'ds.html', {'form': form})
    else:
        form = PhotographerForm()
        return render(request, 'ds.html', {'form': form})


def dashbosrd(request):
    album = Album.objects.all()
    return render(request, 'dashboard.html', {'album': album})


def addalbum(request):
    if request.method == 'POST':
        form = AlbumAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form = AlbumAddForm(initial={'profile': request.user.profile.id})
        return render(request, 'create.html', {'form': form})


def addphoto(request, album_id):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        form = AlbumAddPhotoForm(request.POST, request.FILES, initial={'tag': request.POST['tag']})
        form.save()
        return HttpResponseRedirect(reverse('profile'))
    form = AlbumAddPhotoForm(initial={'album': album_id})
    return render(request, 'ds.html', {'form': form})

# def viewphoto(request,album_id):
