from django.urls import path
from .views import *
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

app_name="experience"
urlpatterns = [
      path('add', add_experience, name='add_experience'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)