from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Janri,Track
from django.shortcuts import render
from .forms import AddForm, AddFormTracks
# from .models import Track
# Create your views here.
def main(request):
    return render(request, 'index.html')
    
def genres(request):
    janri = Janri.objects.all()
    return render(request, 'genres.html',{'janri':janri})

def tracks(request):
    Tracks = Track.objects.all()
    return render(request, 'tracks.html',{'Tracks':Tracks})

def deleteop(request,id_genres):
    genres = Janri.objects.get(id=id_genres)
    genres.delete()
    return HttpResponse('<h1> Жанр успешно удален</h1><br><a href="/janri/">На главную</a>')

def add_genre(request):
    if request.method == "POST":
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        desc = request.POST.get("description")
        genre = Janri ()
        genre.name_ru = name_ru
        genre.name_en = name_en
        genre.description = desc
        genre.save()
        return redirect('/janri/')
    else:
        genreform = AddForm()
        return render(request, "add_genre.html", {'form': genreform})

def edite(request,id_genres):
    g = Janri.objects.get(id=id_genres)

    if request.method == "POST":
        genre = AddForm (request.POST, instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/janri/')
    else:
        genreform = AddForm(instance=g)
        return render(request, "edit.html", {'form': genreform})

    






def delete_track(request,id_genres):
    track = Track.objects.get(id=id_genres)
    track.delete()
    return HttpResponse('<h1> Трек успешно удален</h1><br><a href="/Tracks/">На главную</a>')

def add_track(request):
    if request.method == "POST":
        title = request.POST.get("title")
        duration = request.POST.get("duration")
        name_en = request.POST.get("{{g.name_en}}")
        track = Track ()
        track.title = title
        track.duration = duration
        track.name_en = name_en
        track.save()
        return redirect('/Tracks/')
    else:
        trackform = AddFormTracks()
        return render(request, "add_genre.html", {'form': trackform})

def edite_track(request,id_genres):
    g = Janri.objects.get(id=id_genres)

    if request.method == "POST":
        genre = AddForm (request.POST, instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/janri/')
    else:
        trackform = AddForm(instance=g)
        return render(request, "edit.html", {'form': trackform})