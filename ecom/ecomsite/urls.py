from django.urls import path
from . import views

app_name = 'ecomsite'

urlpatterns = [
    path('',views.index, name = "index"),
    path('about/',views.about,name = "about"),
    path('analyze',views.analyze, name = "analyze"),
    path('removepunc', views.removepunc, name='rempun'),
    
    # path('capitalizefirst', views.capfirst, name='capfirst'),
    # path('newlineremove', views.newlineremove, name='newlineremove'),
    # path('spaceremove', views.spaceremove, name='spaceremove'),
    # path('charcount', views.charcount, name='charcount'),

]
