from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('kolabadmin/', admin.site.urls),
    path('', include('home.urls')),
    path('projects/', include('projects.urls')),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path('board/', include('board.urls')),
    path('people/', include('people.urls')),
    path('publication/', include('publication.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

