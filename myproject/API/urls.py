from django.urls import path
from .views import ProjectCreate


urlpatterns = [
  path('project/create', ProjectCreate.as_view())
]
