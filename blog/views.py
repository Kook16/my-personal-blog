from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse

from .models import Post, Author, Tag
from .forms import CommentForm
# Create your views here.

all_posts = Post.objects.all()

# def get_date(post):
#     return post.date


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]

 
# def starting_page(request):
#     sorted_posts = sorted(all_posts, key=get_date)
#     lastest_post = sorted_posts[-3:]
#     return render(request, "blog/index.html", {
#         'posts': lastest_post
#     })


class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


# def posts(request):
#     return render(request, 'blog/all-posts.html', {
#         'all_posts': all_posts
#     })


class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later


    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            'post': post,
            'post_tags': post.tag.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)
    
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tag.all(),
            'comment_form': comment_form, 
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)

    
# def post_detail(request, slug):
#     idenified_post = next(
#         post for post in all_posts if post.slug == slug)
#     return render(request, 'blog/post-detail.html', {
#         'post': idenified_post,
#         'post_tags': idenified_post.tag.all()
#     })

class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)


    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if not stored_posts:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')