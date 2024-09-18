from django.shortcuts import render, redirect
# from datetime import date
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView  # Importing generic views for list and detail views.
from django.views import View  # Importing the View class for custom class-based views.
from django.urls import reverse  # Importing reverse for redirection after form submission.

from .models import Post, Author, Tag  # Importing models used in the views.
from .forms import CommentForm  # Importing the comment form.

# Querying all posts from the database.
all_posts = Post.objects.all()

# def get_date(post):
#     return post.date

# Class-based view for the starting page (home page).
class StartingPageView(ListView):
    template_name = 'blog/index.html'  # Specifies the template to use for rendering.
    model = Post  # Specifies the model to query (Post model).
    ordering = ['-date']  # Orders the posts by date, descending.
    context_object_name = 'posts'  # Names the context variable for use in the template.

    # Overriding the default queryset to limit the number of posts displayed (only the 3 most recent).
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]

# Function-based view (commented out) for the starting page. It was replaced by the class-based view above.
# def starting_page(request):
#     sorted_posts = sorted(all_posts, key=get_date)
#     lastest_post = sorted_posts[-3:]
#     return render(request, "blog/index.html", {
#         'posts': lastest_post
#     })

# Class-based view for displaying all posts.
class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'  # Specifies the template for rendering.
    model = Post  # Specifies the model to query (Post model).
    ordering = ['-date']  # Orders the posts by date, descending.
    context_object_name = 'all_posts'  # Names the context variable for use in the template.

# Function-based view (commented out) for displaying all posts. It was replaced by the class-based view above.
# def posts(request):
#     return render(request, 'blog/all-posts.html', {
#         'all_posts': all_posts
#     })

# Class-based view for displaying a single post and handling comments.
class SinglePostView(View):
    
    # Helper function to check if the current post is saved in the user's session for later reading.
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts:
            is_saved_for_later = post_id in stored_posts  # Checks if post_id is in stored posts.
        else:
            is_saved_for_later = False
        return is_saved_for_later

    # GET request handler for displaying a single post by its slug.
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)  # Retrieves the post by its slug.
        
        # Context data passed to the template for rendering.
        context = {
            'post': post,  # The post itself.
            'post_tags': post.tag.all(),  # Tags associated with the post.
            'comment_form': CommentForm(),  # The empty comment form.
            'comments': post.comments.all().order_by('-id'),  # All comments related to the post.
            'saved_for_later': self.is_stored_post(request, post.id)  # Check if post is saved for later.
        }
        return render(request, 'blog/post-detail.html', context)  # Render the post detail page.
    
    # POST request handler for submitting a new comment.
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)  # Retrieves the post by its slug.
        comment_form = CommentForm(request.POST)  # Bind form data from POST request.

        if comment_form.is_valid():  # Check if the form is valid.
            comment = comment_form.save(commit=False)  # Save the form but don't commit to DB yet.
            comment.post = post  # Assign the post to the comment.
            comment.save()  # Save the comment to the database.
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))  # Redirect to the same post detail page.

        # If the form is invalid, re-render the page with the existing data and errors.
        context = {
            'post': post,
            'post_tags': post.tag.all(),
            'comment_form': comment_form,  # Re-render the form with errors.
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)

# Function-based view (commented out) for displaying a single post. It was replaced by the class-based view above.
# def post_detail(request, slug):
#     idenified_post = next(
#         post for post in all_posts if post.slug == slug)
#     return render(request, 'blog/post-detail.html', {
#         'post': idenified_post,
#         'post_tags': idenified_post.tag.all()
#     })

# Class-based view for handling 'Read Later' functionality.
class ReadLaterView(View):

    # GET request handler for displaying saved posts.
    def get(self, request):
        stored_posts = request.session.get("stored_posts")  # Retrieve stored post IDs from the session.

        context = {}

        # If no posts are stored, show an empty list.
        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)  # Retrieve the stored posts by their IDs.
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)  # Render the stored posts page.

    # POST request handler for adding/removing posts from the saved list.
    def post(self, request):
        stored_posts = request.session.get('stored_posts')  # Retrieve stored post IDs from the session.

        if not stored_posts:
            stored_posts = []

        post_id = int(request.POST["post_id"])  # Get the post ID from the form.

        if post_id not in stored_posts:
            stored_posts.append(post_id)  # Add the post to the saved list if not already saved.
        else:
            stored_posts.remove(post_id)  # Remove the post from the saved list if it's already saved.

        request.session['stored_posts'] = stored_posts  # Save the updated list to the session.

        return HttpResponseRedirect('/')  # Redirect to the home page after saving.
