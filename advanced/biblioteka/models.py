from django.db import models

class Author(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=False, default=None)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=50,blank=False)
    rok_wydania = models.IntegerField(blank=False)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.tytul