# Importiert vorhandene Objekte
from django.conf import settings
from django.db import models
from django.utils import timezone

# hier wird unser Objekt (Klasse/Model) definiert
class Post(models.Model):
    # class: eine Klasse
    # Post: Der Name des neu geschaffenen Model's:
    # models.Model: das neue Model mit NAmen 'Post' ist ein Django-Model,
    # es soll also in der DB gespeichert werden
    #
    # die Felder/Eigenschaften werden definiert (festgelegt):
    # von welchem (Daten-) Typ ist das neue Feld,
    # in welcher Beziehung steht es zu den anderen Objekten, ...
    #
    # models.ForeignKey – definiert eine Verknüpfung/Beziehung zu einem anderen Model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.CharField – ein Textfeld mit max. 200 Zeichen
    title = models.CharField(max_length=200)
    # models.TextField – ein langes Textfeld ohne Grössenbeschränkung,
    # perfekt für die Inhalte eines Post in einem Blog
    text = models.TextField()
    # models.DateTimeField – aktueller Zeitstempel:
    # ein Feld für das aktuelle Datum mit Uhrzeit
    created_date = models.DateTimeField(default=timezone.now)
    # Datumsfeld mit leerem (?) Inhalt
    published_date = models.DateTimeField(blank=True, null=True)

    # die neue Methode (=Fkt. einer Klasse) publish(..) zum
    # Veröffentlichen eines neuen Post im Blog,
    # hier wird das Datum der Veröffentlixhung gesetzt und gespeichert
    #
    # beide Methoden sind eingerückt => Gehören zur Klasse, können
    # nur mit Objekten der Klasse verwendet werden
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
