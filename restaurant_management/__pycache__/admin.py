from django .contrib import admin
from.models import Menu, Order, OrderItem

class OrderItemInline(addmin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    search_fields = ("name",)

@admin.register(Order)
class OrderItem(admin.ModelAdmin):
    list_display = ("id", "customer", "total_amount", "status", "created_at")
    list_filter = ("status", "created_at")
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "menu_item", "quantity")