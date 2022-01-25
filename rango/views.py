from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category

def index(request):
    # Query the database for the top 5 categories
    category_list = Category.objects.order_by('-likes')[:5]

    # Create a dict which django will use to replace the template variables
    context_dict = {}
    context_dict['boldmessage'] = "Crunchy, creamy, cookie, candy, cupcake!"
    context_dict['categories'] = category_list

    # Return the rendered template
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Return the rendered template
    return render(request, 'rango/about.html')