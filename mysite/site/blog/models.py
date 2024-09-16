from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
  cation = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.cation}'
  

class Author(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email_address = models.EmailField(null=True)

  class Meta:
    verbose_name = 'author'
    verbose_name_plural = 'authors'

  def full_name(self):
    return f'{self.first_name} {self.last_name}'


  def __str__(self):
    return self.full_name()
  

class Post(models.Model):
  title = models.CharField(max_length=150)
  excerpt = models.CharField(max_length=200)
  image = models.ImageField(upload_to='posts', null=True)
  date = models.DateField(auto_now=True)
  content = models.TextField(validators=[MinLengthValidator(10)])
  slug = models.SlugField(unique=True, null=True)
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
  tag = models.ManyToManyField(Tag)

  class Meta:
    verbose_name = 'post'
    verbose_name_plural = 'posts'


  def __str__(self):
    return f"{self.title}"
  

class Comment(models.Model):
  user_name = models.CharField(max_length=120)
  user_email = models.EmailField()
  text = models.TextField(max_length=500)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
