from django.shortcuts import render, get_object_or_404
from .models import Entries


def all_blogs(request):
    entries = Entries.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'entries':entries})

def detail(request, blog_id):
    blog = get_object_or_404(Entries, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})

