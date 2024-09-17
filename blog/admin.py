from django.contrib import admin
from .models import Tag, Author, Post, Comment  # Importing the models you want to manage in the admin interface.

# Customizing the admin interface for the Post model.
class PostAdmin(admin.ModelAdmin):
    # Adds filters in the admin panel based on these fields.
    list_filter = ('tag', 'author', 'date',)
    
    # Specifies which fields should be displayed in the list view of posts.
    list_display = ('title', 'date', 'author',)
    
    # Automatically populates the slug field based on the title when creating/editing a post.
    prepopulated_fields = {"slug": ('title',)}

# Customizing the admin interface for the Comment model.
class CommentAdmin(admin.ModelAdmin):
    # Specifies the fields to display in the list view of comments.
    list_display = ('user_name', 'post')

# Register your models here so they appear in the Django admin interface.
admin.site.register(Tag)  # Registers the Tag model.
admin.site.register(Author)  # Registers the Author model.
admin.site.register(Post, PostAdmin)  # Registers the Post model with the custom PostAdmin configuration.
admin.site.register(Comment, CommentAdmin)  # Registers the Comment model with the custom CommentAdmin configuration.
