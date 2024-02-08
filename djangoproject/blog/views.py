from django.shortcuts import render

posts = [
    {
        "author": "MaddieM",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "2024/02/08"
    },
    {
        "author": "AbiN",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "2024/02/09"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
