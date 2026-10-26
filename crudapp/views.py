
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, "crudapp/product_list.html", {
        "products": products
    })


def product_create(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST["name"],
            description=request.POST["description"],
            price=request.POST["price"]
        )
        return redirect("product_list")

    return render(request, "crudapp/product_form.html")


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.save()
        return redirect("product_list")

    return render(request, "crudapp/product_form.html", {
        "product": product
    })


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "crudapp/product_confirm_delete.html", {
        "product": product
    })
