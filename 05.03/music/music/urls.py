from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main),
    path('janri/',views.genres),
    path('Tracks/',views.tracks),
    path('deleteop/<int:id_genres>',views.deleteop),
    path('add_genre/',views.add_genre),
    path('edite/<int:id_genres>',views.edite),
    path('delete_track/<int:id_genres>',views.delete_track),
    path('edite_track/<int:id_genres>', views.edite_track),
    path('add_track/',views.add_track),
    path('artists/', views.artists),
    path('add_artist/', views.add_artist),
    path('editartist/<int:id_artist>', views.editartist),
    path('deleteartist/<int:id_artist>', views.deleteartist),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
