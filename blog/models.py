from django.db import models  # Importing Django's models module to create database models.
from django.core.validators import MinLengthValidator  # Importing a validator to enforce minimum length for fields.

# Model representing a tag, which can be associated with multiple posts.
class Tag(models.Model):
    cation = models.CharField(max_length=255)  # A tag name with a max length of 255 characters.

    # String representation of the tag object (useful in Django admin or shell).
    def __str__(self):
        return f'{self.cation}'

# Model representing an author.
class Author(models.Model):
    first_name = models.CharField(max_length=255)  # Author's first name with a max length of 255 characters.
    last_name = models.CharField(max_length=255)  # Author's last name with a max length of 255 characters.
    email_address = models.EmailField(null=True)  # Author's email address, which can be null.

    # Meta options to specify singular and plural names for the model in the Django admin.
    class Meta:
        verbose_name = 'author'  # Singular form of the model name.
        verbose_name_plural = 'authors'  # Plural form of the model name.

    # Method to return the full name of the author by combining first and last name.
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # String representation of the author object, returning the full name.
    def __str__(self):
        return self.full_name()

# Model representing a blog post.
class Post(models.Model):
    title = models.CharField(max_length=150)  # The title of the post with a max length of 150 characters.
    excerpt = models.CharField(max_length=200)  # A short excerpt or summary with a max length of 200 characters.
    image = models.ImageField(upload_to='posts', null=True)  # An optional image uploaded to the 'posts' folder.
    date = models.DateField(auto_now=True)  # The date the post was created, automatically set to current date.
    content = models.TextField(validators=[MinLengthValidator(10)])  # The main content of the post, requiring at least 10 characters.
    slug = models.SlugField(unique=True, null=True)  # A slug field for the post, ensuring uniqueness and allowing null values.
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    # ForeignKey relationship to the Author model, allowing posts to have an author, and setting to null if the author is deleted.
    
    tag = models.ManyToManyField(Tag)  # A many-to-many relationship to the Tag model (a post can have multiple tags).

    # Meta options to specify singular and plural names for the model in the Django admin.
    class Meta:
        verbose_name = 'post'  # Singular form of the model name.
        verbose_name_plural = 'posts'  # Plural form of the model name.

    # String representation of the post object, returning the title.
    def __str__(self):
        return f"{self.title}"

# Model representing a comment on a post.
class Comment(models.Model):
    user_name = models.CharField(max_length=120)  # The name of the user who made the comment.
    user_email = models.EmailField()  # The email of the user who made the comment.
    text = models.TextField(max_length=500)  # The comment text, with a maximum length of 500 characters.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  
    # ForeignKey relationship to the Post model, linking comments to posts. If a post is deleted, its comments will also be deleted.

    # String representation of the comment could be added for better debugging, but it's optional.
