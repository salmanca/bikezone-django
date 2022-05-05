from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login', views.login , name="login"),
    path('register', views.register , name="register"),
    path('logout', views.logout , name="logout"),
    path('dashboard', views.dashboard , name="dashboard"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
