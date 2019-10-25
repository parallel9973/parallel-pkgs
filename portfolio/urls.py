from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # include our custom app urls here
    path('sauron/', include('sauron.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^', include('background_app.urls', namespace='background'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
