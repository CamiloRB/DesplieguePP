from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Buscador import views

app_name = 'Buscador'

urlpatterns = [
    path('', views.index.as_view(), name="index"),
]