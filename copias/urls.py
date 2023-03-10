from django.urls import path
from . import views

urlpatterns = [
    path("copy/", views.CopyView.as_view()),
    path("copy/<pk>/", views.CopyDetailsView.as_view()),
]