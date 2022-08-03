from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.api.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obbtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
