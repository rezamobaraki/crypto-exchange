from django.urls import include, path

app_name = 'accounts'

urlpatterns = [
    path('auth/', include('accounts.urls.authentication', namespace='authentication'), name='authentications'),
]
