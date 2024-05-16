from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication, permissions
from apps.urls import apps_urlpatterns

from core.swagger.generator import BothHttpAndHttpsSchemaGenerator

main_schema_view = get_schema_view(
    openapi.Info(
        title="Ginza API",
        default_version="v1",
        description="This Documentation shows list of api and will give chance to check them",
        contact=openapi.Contact(email="info@ginza.pro"),
    ),
    public=True,
    authentication_classes=[authentication.BasicAuthentication],
    permission_classes=[permissions.IsAdminUser],
    generator_class=BothHttpAndHttpsSchemaGenerator,

)

app_schema_view = get_schema_view(
    openapi.Info(
        title="Ginza Apps API",
        default_version="v1",
        description="Ginza Apps API Documentation shows list of api and will give chance to check them",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@uic.group"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    authentication_classes=[authentication.BasicAuthentication],
    permission_classes=[permissions.IsAdminUser],
    generator_class=BothHttpAndHttpsSchemaGenerator,
    patterns=apps_urlpatterns,#TODO: change this
)

in_app_schema_view = get_schema_view(
    openapi.Info(
        title="Ginza Bot API",
        default_version="v1",
        description="Ginza Bot API Documentation shows list of api and will give chance to check them",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@ginza.pro"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
    authentication_classes=[authentication.BasicAuthentication],
    generator_class=BothHttpAndHttpsSchemaGenerator,
    patterns=apps_urlpatterns,#TODO: change this
)

panel_schema_view = get_schema_view(
    openapi.Info(
        title="Ginza Apps API",
        default_version="v1",
        description="Ginza Apps API Documentation shows list of api and will give chance to check them",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@ginza.pro"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
    authentication_classes=[authentication.BasicAuthentication],
    generator_class=BothHttpAndHttpsSchemaGenerator,
    patterns=apps_urlpatterns,#TODO: All the urls should be added here
)
