from django.urls import path
from .views import main, user_posts, create_post, view_post, post_comment, post_like, comment_like

urlpatterns = [
    path('', main),
    path('user/<int:userid>', user_posts),
    path('user/create-post', create_post),
    path('post/<int:postid>', view_post),
    path('post/<int:postid>/comment/', post_comment),
    path('post/<int:postid>/like/', post_like),
    path('comment/<int:commentid>/like/', comment_like),
    ]