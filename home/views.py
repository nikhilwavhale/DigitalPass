from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World!</h1><p>Welcome to my first Django project.</p>")