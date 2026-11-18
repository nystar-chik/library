from django.contrib import admin
from django.urls import path, include
from apps.urls import urlpatterns as app
from account.urls import urlpatterns as account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(app)),
    path('api/v1/auth/', include(account)),
    path('api/v1/drf-auth/', include('rest_framework.urls'))
]
