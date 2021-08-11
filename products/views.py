from typing import OrderedDict
from .form import OrderForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

#creating view for home
def home(request):
    #get the details form database
    product_details = products.objects.all()
    allOrders = Order.objects.all()

    context = {
        'product_details': product_details, 'allOrders': allOrders
    }
    return render(request,"products/products.html",context)

def Product_view(request,pk):
    product_view = products.objects.get(id=pk)
    context = { 'product_view':product_view}
    return render(request,"products/product_view.html",context)


def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect("/")
    context = {'form': form}
    return render(request,'products/order.html', context)

#function for updating order
def update_order(request,pk_id):
    order_details = Order.objects.get(id=pk_id)
    update_form = OrderForm(instance=order_details)
    if request.method == 'POST':
        update_form = OrderForm(request.POST, instance=order_details)
        if update_form.is_valid():
            update_form.save()
            return redirect("/")
    
    context = { 'form': update_form }
    return render(request, 'products/order.html', context)

#functions for remove order
def remove_order(request,pk):
    remove_order_details = Order.objects.get(id=pk)
    if request.method == 'POST':
        remove_order_details.delete()
        return redirect("/")
    context = {'remove': remove_order_details}
    return render(request, 'products/remove_order.html',context)