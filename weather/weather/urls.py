from django.contrib import admin
from django.urls import path, include
from locations.views import ListLocations

handler404 = 'core.views.page_not_found'
handler403 = 'core.views.csrf_failure'
handler500 = 'core.views.internal_server_error'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('records/', include('records.urls')),
    path('locations/', include('locations.urls')),
    path('auth/', include('users.urls')),
    path('', ListLocations.as_view(), name='index')
]
