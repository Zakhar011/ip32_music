from django.db import models

# Create your models here.
class Janri(models.Model):
    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    description = models.TextField()
    def  __str__(self):
        return self.name_en
      

class Artist(models.Model):
    name = models.CharField(max_length=500, unique=True)
    image= models.ImageField(upload_to='artists/', null=True)
    def __str__(self):
        return self.name
          
class Track(models.Model):
    title=models.CharField(max_length=100)
    duration=models.IntegerField()
    genres=models.ManyToManyField(Janri)
    artist= models.ForeignKey(Artist, on_delete=models.RESTRICT,null=True)
    def __str__(self):
        return self.title