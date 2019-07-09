from django.urls import path # importiert die Django-Funktion path
from . import views # importiert alle view's aus der blog-Applikation


# path(route, view, kwargs=None, name=None)
urlpatterns = [
    # weil route='' -> Root-URL
    # auf view 'post_list' verwiesen
    # mit name='post_list' wird die view identifiziert
    # sie wird in blog/view.py spezifiziert
    path('', views.post_list, name='post_list'),
    #
    # Abfrage für "...my_website.../post/5/" -> pk=5
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #
    # die Formular-view: name = post_new
    path('post/new/', views.post_new, name='post_new'),
    #
    # Abfrage für "...my_website.../post/3/edit/ -> pk=3
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
