from django.contrib import admin

from orders.models.order import Order


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'crypto', 'amount')
    search_fields = ('user', 'crypto')
    list_filter = ('user', 'crypto')
    ordering = ('user', 'crypto')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('user', 'crypto', 'amount')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
