from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Pizza

#from .forms import OrderForm

def index(request):
  """This view will resolve the index request"""
  return render(request, 'dashboard/index.html')

def menu(request):
  """This page will show all flavors of pizza."""
  pizzas = Pizza.objects.all().order_by('name')
  context = {'pizzas': pizzas}
  return render(request, 'dashboard/menu.html', context)

# def order(request):
#   """This is to place a new order."""
#   if request.method != 'POST':
#     form = OrderForm()
#   else:
#     form = OrderForm(data=request.POST)
#     if form.is_valid():
#       new_order = form.save(commit=False)
#       new_order.save()
#       return redirect('dashboard:index')
#   context = {'form': form}
#   return render(request, 'dashboard/new_order.html', context)
    