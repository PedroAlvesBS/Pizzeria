from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    pizza_number = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    toppings = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'pizzas'

class Order(models.Model):
    order_number = models.IntegerField(auto_created=True, primary_key=True)
    pizza_number = models.ManyToManyField(Pizza)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'orders'

    
    