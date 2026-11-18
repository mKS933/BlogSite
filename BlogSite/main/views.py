from django.shortcuts import render, get_object_or_404

# Create your views here.

def base(request):
    context = {"title": "BlogSite"}
    return render(request, "base.html", context)

def bio(request):
    context = {"title": "BlogSite"}
    return render(request, "bio.html", context)