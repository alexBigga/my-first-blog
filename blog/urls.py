from django.urls import path
from . import views

# create url-pattern, neue view post_list erstellt
# und leite Anfragen dahin um
urlpatterns = [
    path('', views.post_list, name='post_list'),
]