from django.shortcuts import render


def home(request):
    title = "Home"
    content = "This is home page"

    context = {
        "title": title,
        "content": content,
    }
    return render(request, 'page.html', context)


def about(request):
    title = "About"
    content = "This is about page"

    context = {
        "title": title,
        "content": content,
    }
    return render(request, 'page.html', context)
