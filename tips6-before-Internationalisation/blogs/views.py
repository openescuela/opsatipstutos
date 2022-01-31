from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import ContactMe

def index(request):
    posts = Post.objects.all().order_by('publish')
    longerPost = posts[0]
    contactme = ContactMe()

    if request.method == 'POST':
        contactme = ContactMe(data=request.POST)
        if contactme.is_valid():
            new_message = contactme.save(commit=False)
            new_message.save()
            return HttpResponseRedirect(request.path)
    else:
        contactme = ContactMe()

    return render(request, 'blogs/index.html',{'posts':posts,
                                                'longerPost':longerPost,
                                                'contactme':contactme})
