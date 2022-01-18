from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Create a dict which django will use to replace the template variables
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return the rendered template
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Return the rendered template
    return render(request, 'rango/about.html')