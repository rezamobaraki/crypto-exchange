from django.contrib import admin

from exchanges.models.crypto_currency import CryptoCurrency


@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('name', 'price')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'price')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
