from django.urls import path
from . import views

urlpatterns = [
    path("emprestar/<int:pk>/", views.BorrowView.as_view()),
    path("devolver/<int:pk>/", views.BorrowDetailView.as_view()),
    path("copy/", views.CopyView.as_view()),
    path("copy/<pk>/", views.CopyDetailsView.as_view()),
]