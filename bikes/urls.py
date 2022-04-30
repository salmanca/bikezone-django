from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.bike , name="bikes"),
    path('<int:id>/',views.bike_details, name='bike_details'),
    path('search', views.search, name='search'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
