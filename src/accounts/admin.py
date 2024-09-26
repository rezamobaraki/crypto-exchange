from django.contrib import admin

from accounts.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user', 'balance')
    list_filter = ('user', 'balance')
    ordering = ('user', 'balance')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('user', 'balance')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
