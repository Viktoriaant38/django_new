from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, Comment, PostLike, CommentLike

user = get_user_model()

def main(request):
    context = {
        "posts": Post.objects.all().order_by("-pk"),
    }
    return render(request, 'main.html', context)

def user_posts(request, userid):
    context = {
        "posts": Post.objects.filter(author_id=userid).order_by("-pk"),
        "username": user.objects.get(id=userid).username
    }
    return render(request, 'main.html', context)

def view_post(request, postid):
    posts = Post.objects.filter(pk=postid)
    post = Post.first() if posts else None
    context = {
        "post": post,
        "comments": Comment.objects.filter(post=post).order_by("-pk"),
        "user_likes": PostLike.objects.filter(post=post, author = request.user).exists(),
    }
    return render(request, 'post.html', context)

def post_comment(request, postid):
    posts = Post.objects.filter(pk=postid)
    post = posts.first() if posts else None
    if post:
        Comment.objects.create(
            post = post,
            author = request.user,
            text = request.POST.get("text")
        )

    return redirect(f'/post/{postid}')

def post_like(request, postid):
    posts = Post.objects.filter(pk=postid)
    post = posts.first() if posts else None
    referer = request.META.get('HTTP_REFERER')
    if post:
        likes = PostLike.objects.filter(post=post, author = request.user)
        if likes:
            likes.first().delete()
        else:
            PostLike.objects.create(
                post=post,
                author=request.user,
            )
    return redirect(referer)

def comment_like(request, commentid):
    comments = Comment.objects.filter(pk=commentid)
    comment = comments.first() if comments else None
    referer = request.META.get('HTTP_REFERER')
    if comment:
        likes = CommentLike.objects.filter(comment=comment, author = request.user)
        if likes:
            likes.first().delete()
        else:
            CommentLike.objects.create(
                comment=comment,
                author=request.user,
            )
    return redirect(referer)



@login_required
def create_post(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Post.objects.create(text = text, author = request.user)
            return redirect("/")
        return render(request, 'create_post.html', context = {"error": "Text can't be empty"})
    return render(request, 'create_post.html',)
# Create your views here.
