from django import forms # -> Formulare
from .models import Post # -> unser Model vom blog

# ModelForm speichert den Inhalt des Formulars in das Model

# PostForm: Name unseres eigenen Formulars

# forms.ModelForm: Fuer unser Formular sollen die Methoden von ModelForm zur Verwendung bereit stehen
class PostForm(forms.ModelForm):

    # class Meta:
    # Erstelle fuer das importierte Model Post ein Formular
    class Meta:
         model = Post
         # welche Felder soll das Formular verwenden:
         fields = ('title', 'text',)

# Jetzt:
#   - in einer view benutzen, dazu Link auf eine Seite mit dem Formular
#   - im Template darstellen
