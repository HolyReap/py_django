from django.http import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    orders = {
        "name" : "name",
        "min_price" : "price",
        "max_price" : "-price"
    }
    order = request.GET.get('sort',"name")
    catalog = Phone.objects.all().order_by(orders[order])
    phones = [item.__dict__ for item in catalog]
    
    template = 'catalog.html'
    context = {"phones" : phones}
    return render(request, template, context)


def show_product(request, slug):
    #product = list(Phone.objects.filter(slug = slug))
    #this_phone = {
    #    "name" : product[0].name,
    #    "price" : product[0].price,
    #    "image" : product[0].image,
    #    "release_date" : product[0].release_date,
    #    "lte_exists" : product[0].lte_exists,
    #    "slug" : product[0].slug
    #}
    this_phone = Phone.objects.get(slug=slug)
    product = this_phone.__dict__
    template = 'product.html'
    context = {"phone" : product}
    return render(request, template, context)

def test(request):
    data = Phone.objects.all()
    out = [f'{item.id}, {item.name}, {item.price}, {item.image}, {item.release_date}, {item.lte_exists}, {item.slug}' for item in data]
    return HttpResponse(out)