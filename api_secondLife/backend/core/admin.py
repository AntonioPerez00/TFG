from django.contrib import admin
from .models import User, Category, Rating, Product, Photo, Order, Offer

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Order)
admin.site.register(Offer)
