from django.urls import path
from . import views

urlpatterns = [
    path("borrow/history/", views.BorrowListView.as_view()),
    path("borrow/history/<int:pk>/", views.BorrowListCollaboratorView.as_view()),
    path("borrow/<int:pk>/", views.BorrowView.as_view()),
    path("return/<int:pk>/", views.BorrowDetailView.as_view()),
    path("copy/", views.CopyView.as_view()),
    path("copy/<pk>/", views.CopyDetailsView.as_view()),
]