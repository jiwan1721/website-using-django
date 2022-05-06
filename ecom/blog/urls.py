from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.index, name = "blogHome"),
    path('about/',views.about, name = "blogAbout"),
    path('contact/',views.contact,name = "blogContact"),
    path('tracker/',views.contact,name = "blogtracker"),
    path('search/',views.contact,name = "blogsearch"),
    path('productView/',views.contact,name = "blogproductView"),
    path('checkout/',views.contact,name = "blogcheckout"),
]