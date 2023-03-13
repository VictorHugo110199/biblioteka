from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<pk>/", views.BookDetailsView.as_view()),
    path("books/following/", views.GetFollowingView.as_view()),
    path("books/<int:book_id>/follow/", views.FollowingView.as_view()),
    path("books/unfollow/<int:book_id>/", views.UnfollowView.as_view()),
]