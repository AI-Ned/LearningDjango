from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()

    # The render funtion pulls through the HTML template, it also allows for a dictionary to populate variables outlined on the HTML template. 
    return render(
        request, 
        "HelloDjangoApp/index.html",
            {
                'title':"Hello Django!",
                'message':"Hello World",
                'content':" on " + now.strftime("%A, %d %B, %Y, at %X")
            }
        )
