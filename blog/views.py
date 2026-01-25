from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post

def main(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'main.html', context)

def user_posts(request, userid):
    context = {
        'posts': Post.objects.filter(author_id=userid),
    }
    return render(request, 'main.html', context)

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
