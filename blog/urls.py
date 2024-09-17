from django.urls import path  # Importing the path function to define URL patterns.
from . import views  # Importing the views from the current directory.

# URL patterns for the blog application.
urlpatterns = [
    # URL pattern for the homepage or starting page.
    # It maps the root URL ('') to the StartingPageView class-based view.
    path('', views.StartingPageView.as_view(), name="starting-page"),
    
    # URL pattern for the 'All Posts' page.
    # It maps 'post/' to the AllPostsView class-based view, showing all blog posts.
    path('post/', views.AllPostsView.as_view(), name="posts-page"),
    
    # URL pattern for individual post detail pages.
    # The URL includes a slug as a dynamic part that identifies the post.
    # It maps 'post/<slug:slug>/' to the SinglePostView class-based view.
    path('post/<slug:slug>/', views.SinglePostView.as_view(), name='post-detail-page'),
    
    # URL pattern for the 'Read Later' functionality.
    # It maps 'read-later' to the ReadLaterView class-based view, allowing users to save posts for later reading.
    path("read-later", views.ReadLaterView.as_view(), name='read-later')
]
