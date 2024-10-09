from django.contrib import admin
from transactions.models.transaction import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'amount', 'content_type', 'object_id', 'type')
    search_fields = ('wallet', 'amount', 'content_type__model', 'object_id', 'type')
    list_filter = ('wallet', 'amount', 'content_type', 'type')
    ordering = ('wallet', 'amount', 'content_type', 'object_id', 'type')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('wallet', 'amount', 'content_type', 'object_id', 'type')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
