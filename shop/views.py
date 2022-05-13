from django.shortcuts import render

from .models import Product


# Create your views here.
def index(request):
    slider_products = Product.objects.filter(show_in_slider=True).all()
    recommended_products = Product.objects.filter(is_recommended=True).all()
    new_year_sale_products = Product.objects.filter(is_new_year_sale=True).all()

    return render(request, "index.html", {
        "slider_products": slider_products,
        "recommended_products": recommended_products,
        "new_year_sale_products": new_year_sale_products,
    })


def product(request):
    return render(request, "product.html")


def cart(request):
    return render(request, "cart.html")


def not_found(request):
    return render(request, "404.html")
