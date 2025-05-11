from django.contrib import admin
from .models import User, Category, Rating, Product, Order, Offer

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Offer)
