from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello_world_app.urls'))
    path('api/', include('check_api_app.urls'))
]
