from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.template import loader

def index(request):
    latest_category_list = Categories.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.name for q in latest_category_list])
    template = loader.get_template('products/index.html')
    context = {
	'latest_category_list': latest_category_list,
    } 
    return HttpResponse(template.render(context, request))
    # return HttpResponse(output)
    # return HttpResponse("%s" % "this page is working")
def detail(request, category_id):
    category = get_object_or_404(Categories, pk=category_id)
    return render(request, 'products/detail.html', {'category': category}) 
'''def detail(request, category_id):
    try:
        category = Categories.objects.get(pk=category_id)
    except Categories.DoesNotExist:
        raise Http404("Category Does not exist")
    return render(request, 'products/detail.html', {'category':category})
'''
