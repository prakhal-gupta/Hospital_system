from django.contrib import admin
from django.urls import include,path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Patient/', include('PatientV.urls')),
    path('Doctor/', include('DoctorV.urls')),
    path('Receptionist/', include('ReceptionistV.urls')),
    path('admin/', admin.site.urls),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
