from django.urls import path

from .apps import AppConfig
from .views import custom_function

app_name = AppConfig.app_url

urlpatterns = [
    path(f"api/v1/apps/{app_name}/custom_url/", custom_function, name="custom_class_view"),

]
