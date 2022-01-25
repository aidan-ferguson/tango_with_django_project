from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page

def index(request):
    # Query the database for the top 5 categories by likes (desc)
    category_list = Category.objects.order_by('-likes')[:5]

    # Query the database for the top 5 pages by views (desc)
    page_list = Page.objects.order_by('-views')[:5]

    # Create a dict which django will use to replace the template variables
    context_dict = {}
    context_dict['boldmessage'] = "Crunchy, creamy, cookie, candy, cupcake!"
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    # Return the rendered template
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Return the rendered template
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        # Query for a category with given slug 
        category = Category.objects.get(slug=category_name_slug)

        # Get all pages in that category
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        # Can't find provided category
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)