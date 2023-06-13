from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings
from core.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
