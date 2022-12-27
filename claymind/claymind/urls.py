from django.contrib import admin
from django.urls import path

from core.views import index, order_database

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('order_database/', order_database, name='order_database'),
]
