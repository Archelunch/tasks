from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.forms import *
from django.http import HttpResponseRedirect
from blog.models import Post, Comment
# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request,
    'post.html',
    {'form': form}
    )

@login_required
def post_page(request, id):
    try:
        post = Post.objects.get(pk=id)
        comments = post.comments.all()
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.com = post
                comment.save()

        else:
            form = CommentForm()
        return render(request,
        'post_page.html',
        {'form': form, 'post': post, 'comments':comments}
        )

    except Exception as e:
        print(e)
        return render(request,
        'post_page.html',
        {'alert': "Такого поста нет"}
        )


@login_required
def feed(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'posts.html', {'posts':posts})
