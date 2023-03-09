from django.urls import path
from . import views

urlpatterns = [
    path("copias/", views.CopyView.as_view()),
    path("copias/<int:pk>/", views.CopyDetailView.as_view()),
    path("emprestar/<int:pk>/", views.BorrowView.as_view()),
    path("devolver/<int:pk>/", views.BorrowDetailView.as_view()),
]