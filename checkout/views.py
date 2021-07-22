from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JG6R1HG59td0BNz0BHTuxmfLVujuKSLjUttAGwKgQenaJxEhrL1PIcAZU7FNzvL0HzcO9lj3yRqS4nlWfGF8lYh00Mxo9u2qc',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
