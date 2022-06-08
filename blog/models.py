from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.foreignKey(
        User, on_delete=models.CASCADE, related_name="blog-posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured-image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManytoManyField(User, related_name="blog-likes", blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()


class comment(models.Model):
    post = models.foreignKey(
        Post, on_delete=models.CASCADE, related_name="blog-comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Comment {self.body} by {self.name}'