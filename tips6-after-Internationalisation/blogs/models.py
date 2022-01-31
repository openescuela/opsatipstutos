from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

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
    email = models.EmailField(help_text=_("Your email address will not be published"), verbose_name=_("Email"))
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self):
        return self.name
