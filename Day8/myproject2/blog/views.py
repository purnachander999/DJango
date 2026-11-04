from django.http import HttpResponse

# Create your views here.

def post_details(request, post_id):
    return HttpResponse(f"<h1>Show Blog post: {post_id}")

def user(request, username):
    return HttpResponse(f"<h1>Show profile of user: {username}</h1")

def article_details(request, **kwargs):
    return HttpResponse(f"<h1>Data : {kwargs['year']}</h1>")