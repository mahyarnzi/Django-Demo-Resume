from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from resume.setting.dev import STATIC_ROOT, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('summernote/', include('django_summernote.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)