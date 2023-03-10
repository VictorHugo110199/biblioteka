from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<pk>/", views.BookDetailsView.as_view()),
    path("books/<int:book_id>/follow/<int:user_id>/", views.FollowingView.as_view()),
]