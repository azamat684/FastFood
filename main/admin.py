from django.contrib import admin
from .models import Category,Order,OrderItem,Food,Client

admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Client)




