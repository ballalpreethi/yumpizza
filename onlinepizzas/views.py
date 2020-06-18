from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'welcome.html')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            username = form.data["username"]
            password = form.data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next is not None:
                    return redirect("menu_view")
                else:
                    return redirect("index")
            else:
                return render(request, "welcome.html", {"message": "Invalid username/password"})
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'registration/login.html', context)
    else:
        return redirect("index")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, 'register.html', context)


@login_required
def menu_view(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu.html', {"pizzas": pizzas})


@login_required
def confirm_order(request):
    quantities = request.POST.getlist('qty')
    pizzas = Pizza.objects.all()
    ordered_pizzas = []
    ordered_quantities = []
    # prices = request.POST.getlist('price')
    totals = []
    for item, qty in zip(pizzas, quantities):
        if int(qty) > 0:
            ordered_pizzas.append(item)
            ordered_quantities.append(int(qty))
            totals.append(item.price * int(qty))
    return render(request, 'order_confirmation.html', {"order_summary": zip(ordered_pizzas, ordered_quantities, totals),
                                                       "grand_total": sum(totals) + 5,
                                                       "grand_total_usd": round(float(sum(totals) + 5) * 1.12, 2)})


@login_required
def place_order(request):
    quantities = request.POST.getlist('qty')
    pizzas = request.POST.getlist('pizza')
    order = Order(user=request.user)
    order.save()

    for item, qty in zip(pizzas, quantities):
        pizza = Pizza.objects.filter(name=item)
        order_details = OrderDetails(itemId=pizza.first(), orderId=order, Qty=qty)
        order_details.save()

    return render(request, 'order.html')


@login_required
def user_orders_view(request):
    orders = Order.objects.filter(user=request.user)
    user_order_details = OrderDetails.objects.none()
    my_orders = {}
    for order in orders:
        order_details = OrderDetails.objects.filter(orderId=order.id)
        my_orders[order.order_timestamp] = order_details
        user_order_details |= order_details
    context = {"orders": my_orders}
    return render(request, 'my_orders.html', context)
