from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('confirmacion', views.confirmacion, name='confirmacion'),
    path('form_personas', views.form_personas, name='form_personas'),
    path('confirmacion_2', views.confirmacion_2, name='confirmacion_2'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)