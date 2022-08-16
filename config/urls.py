from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings

schema_view = get_schema_view(
    openapi.Info(
        title="API_Blog",
        default_version='v1',
        description="Test description",

    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
    authentication_classes=[]
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("blog.api.urls")),
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui("swagger",
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('sredoc/', schema_view.with_ui("redoc",
                                        cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
