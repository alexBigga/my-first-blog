"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    # wenn die url lautet: "127.0.0.1:8000/admin_1", dann wird das Pattern mit route="admin_1" abgeglichen
    # hier gibt es dazu die view="admin.site.urls"
    # die Datei dazu ist wo?
    #   # ??? Im Ordner admin/site/urls.py ???
    # evtl. besser mit den späteren Aktionen / views: "post->new" und "post->edit" untersuchen
    #
     # path(route, view, kwargs=None, name=None)
    path('admin_1/', admin.site.urls),
    #
    # ist route="", dann kommt view "blog.urls" zurück, dies
    # wird später dazu genutzt, um alle leeren urls die view für Port 8000 auszuliefern
    # wo liegt die Datei zur view "blog.urls"?
    #   # gehe zu blog/urls.py, dort müssen leere route verarbeitet werden
    #
    # einbinden eines Python-Importpfades zu einem anderen URLconf-Modul
    path('', include('blog.urls')),
]
