from django.contrib import admin
from . models import Product, Customer, Cart, Wishlist, Order
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price',
                    'category', 'product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality',
                    'city', 'state', 'zipcode', 'created_at']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

    def products(self, obj):
        link = reverse('admin:app_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','is_paid', 'amount',
                    'customer', 'created_at')


@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products']

    def products(self, obj):
        link = reverse('admin:app_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


admin.site.unregister(Group)
