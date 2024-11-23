from django.urls import path
from django.conf.urls.static import static

from APPSECU import settings
from securité import views


urlpatterns = [
    path('', views.index, name='index'),
    path('voiture/', views.voiture, name='voiture'),
    path('ajout_voiture/', views.ajout_voiture, name='create_voiture'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)