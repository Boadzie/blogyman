from django.urls import path

from .views import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
    SearchResultsListView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
