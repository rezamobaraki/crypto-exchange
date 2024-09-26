from django.urls import include, path

app_name = "transactions"

urlpatterns = [
    path("", include("transactions.urls.transaction", namespace="transaction"), name="transaction"),
]
