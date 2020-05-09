from django.urls import path, include
from . import views
from .views import ChapterPostListView,PostDetailView , CommentCreateView, public_profile, CommentUpdateView, CommentDeleteView, FollowerListView, PostDeleteView, PostUpdateView, likePost, SearchListView, PostListView, ExploreListView, PublicPostListView
import notifications.urls


# second- truncated request is sent here and a match is searched for in url patterns again
urlpatterns = [
    path('logged/', PostListView.as_view(), name='home'),
    path('', PublicPostListView.as_view(), name='public-home'),
    path('chapter/<int:chapter_id>/', ChapterPostListView.as_view(), name='chapter-home'),
    path('explore/', ExploreListView.as_view(), name='explore'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name='comment-form'),
    path('profile/<str:username>/', views.public_profile, name='public-profile'),
    path('post/new/', views.post, name='post-add'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/<str:username>/followers/', views.FollowerListView.as_view(), name='follower-list'),
    path('profile/<str:username>/following/', views.FollowerListView.as_view(), name='following-list'),
    path('post/<int:pk>/likes/', views.LikeListView.as_view(), name='likes-list'),
    path('search/', views.SearchListView.as_view(), name="search-list"),
    path('likepost/', views.likePost, name='likepost'),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
