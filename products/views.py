from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Product
from .forms import ProductFilterForm

def index(request):
    products = Product.objects.all().order_by('name')
    form = ProductFilterForm(request.GET)
    name_search = request.GET.get('name_search')
    sort = request.GET.get('sort')
    min_price = form['min_price'].value()
    max_price = form['max_price'].value()
    if name_search:
        products = products.filter(name__icontains=name_search)
    if sort:
        if sort == 'ages':
          products = products.order_by('minimum_age_appropriate')
        else:
          products = products.order_by(sort)
    if min_price:
      products = products.filter(price__gte=min_price)
    if max_price:
      products = products.filter(price__lte=max_price)
      

    context = {'products': products, 'form': form}
    return render(request, 'products/index.html', context)

def show(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    context = { 'product':p }
    return render(request, 'products/show.html', context)
    
