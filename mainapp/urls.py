from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.test, name = 'test'),
    #path('about',views.about, name = 'about'),
    #path('test',views.test, name = 'test')
]