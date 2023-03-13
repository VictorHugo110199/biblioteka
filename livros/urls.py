from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<pk>/", views.BookDetailsView.as_view()),
    path("books/<int:book_id>/follow/", views.FollowingView.as_view()),
    path("books/following", views.FollowingDetailView.as_view()),
]