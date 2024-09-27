from django.urls import include, path

app_name = 'orders'

urlpatterns = [
    path('', include('orders.urls.order', namespace='order'), name='order'),
]
