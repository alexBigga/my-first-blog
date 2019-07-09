from django.shortcuts import render # praktische Helferlein ...
from django.utils import timezone
# importiert aus dem identischen Verzeichnis / Ordner (bzw. App)
# da models.py im identischen Verzeichnis entfaellt '.py'
from .models import Post
from django.shortcuts import render, get_object_or_404

# Formulare importieren
from .forms import PostForm
# importiere Moeglichkeit zur Weiterleitung
from django.shortcuts import redirect

# Create your views here.

# Fkt-Name identisch zum view-Namen !!!
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # posts:            Query-Set, nach 'published_date' sortiert
    # request:          Anfrage vom user
    # Template-Namen:   blog/post_list.html
    # {}:               Zur Verwendung durch das Template, hier fuer die Variable posts
    #
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # Kombiniert / matched ein template mit einem context-Dictionary,
    # gibt ein Http-Response-Objekt mit dem gerenderten Text zurueck,
    # d.h. sie rendert das Template 'blog/post_detail.html' zu einer fertigen HTML-Seite
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# view fuer die Formulare:
def post_new(request):
    # in welcher Variante geht der hhtp-request ein:
    # 1) schon vorhandener blog-Eintrag:
    if request.method == "POST":
        # uebergebe den Inhalt vom request
        form = PostForm(request.POST)
        # pruefe Eingabe auf Gueltigkeit
        if form.is_valid():
            # Formular speichern, noch nicht commiten
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # wenn fertig, dann gebe die Seite vom soeben erstellten blog-Post aus
            # view-name: post_detail
            return redirect('post_detail', pk=post.pk)
    # Erstbeitrag: Setelle leeres Formular bereit
    elif request.method == "GET":
        # initialisiere leer:
        form = PostForm()
    else:
        return 0
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
