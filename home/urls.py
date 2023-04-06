
from django.urls import path, include
from home.views import BlogView, PublicBlogView, SingleBlogView, CommentView

urlpatterns = [
    path('me/posts/', BlogView.as_view()),
    path('posts/', BlogView.as_view()),
    path('posts/<id>/', BlogView.as_view()),
    path('all/posts/', PublicBlogView.as_view()),
    path('single/posts/<id>/', SingleBlogView.as_view()),
    path('posts/<post_id>/comments/', CommentView.as_view()),
     path('posts/<post_id>/comments/<id>', CommentView.as_view()),
]

