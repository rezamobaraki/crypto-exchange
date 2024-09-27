from django.contrib import admin

from transactions.models.transaction import Transaction


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ('wallet', 'amount', 'order_id', 'type')
    search_fields = ('wallet', 'amount', 'order_id', 'type')
    list_filter = ('wallet', 'amount', 'order_id', 'type')
    ordering = ('wallet', 'amount', 'order_id', 'type')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('wallet', 'amount', 'order_id', 'type')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
