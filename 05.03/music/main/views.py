from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Janri,Track, Artist
from django.shortcuts import render
from .forms import AddForm, AddFormTracks, ArtistForm
# from .models import Track
# Create your views here.
def main(request):
    return render(request, 'index.html')
    
def genres(request):
    janri = Janri.objects.all()
    return render(request, 'genres.html',{'janri':janri})

def tracks(request):
    t = Track.objects.all()
    
    a = Artist.objects.all()
    artist = None
    if request.method == "POST":
        id_artist = request.POST.get('artist')
        if id_artist: 
            artist = Artist.objects.get(id=id_artist)
            t = Track.objects.filter(artist=artist)

    return render(request, 'tracks.html', {'tracks': t, 'artists': a, 'current_artist': artist})

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

    
def artists(request):
    a = Artist.objects.all()
    return render (request, 'artists.html', {'artists':a})

def add_artist(request):
    if request.method == "POST":
        # Передаем не только текст (POST), но и файлы/картинки (FILES)
        form = ArtistForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('/artists/') # После сохранения идем к списку артистов
    else:
        form = ArtistForm()
        
    return render(request, "add_artist.html", {'form': form})
def editartist(request, id_artist):
    artist = Artist.objects.get(id=id_artist)

    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('/artists/') # Возвращаем к списку артистов
    else:
        form = ArtistForm(instance=artist)
        
    return render(request, "edit.html", {'form': form})

def deleteartist(request, id_artist):
    artist = Artist.objects.get(id=id_artist)
    artist.delete()
    return HttpResponse('<h1>Исполнитель успешно удален</h1><br><a href="/artists/">Вернуться к списку</a>')


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

def edite_track(request, id_genres):
    track = Track.objects.get(id=id_genres)

    if request.method == "POST":
        form = AddFormTracks(request.POST, instance=track)
        
        if form.is_valid():
            form.save()
            return redirect('/Tracks/')
    else:
        form = AddFormTracks(instance=track)
        
    return render(request, "edit.html", {'form': form})