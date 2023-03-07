from django.urls import path
from . import views
from .views import CopyView, CopyDetailView

urlpatterns = [
    path("copias/", views.CopyView.as_view()),
    path("copias/<int:pk>/", views.CopyDetailView.as_view()),
]