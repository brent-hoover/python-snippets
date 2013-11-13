from commerce.catalog.models import Product
from commerce.order.models import Order, OrderItem, OrderStatus
from commerce.checkout.models import Customer, Address
from commerce.order.forms import OrderHeaderAdminForm
from django.contrib import admin


class OrderHeaderAdmin(admin.ModelAdmin):
    list_display = ('id','order_created','finalized','exported')
    list_display_links = ('id',)
    #inlines = [OrderItemInline]
    exclude = ('alchemy_user',)
    
admin.site.register(Order, OrderHeaderAdmin)

