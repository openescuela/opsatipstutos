from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    resume = models.TextField()
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category')

    def __str__(self):
        return self.title

class ContactMe(models.Model):
    email = models.EmailField(help_text="Your email address will not be published", verbose_name="Email")
    name = models.CharField(max_length=50, verbose_name="Name")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.name
