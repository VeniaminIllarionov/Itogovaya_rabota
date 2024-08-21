from django.urls import path
from django.views.decorators.cache import cache_page

from services.apps import ServicesConfig
from services.views import (contacts, ServiceDetailView, ServiceListView, ServiceCreateView, ServiceUpdateView,
                            ServiceDeleteView)

app_name = ServicesConfig.name

urlpatterns = [
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('', ServiceListView.as_view(), name='home'),
    path('edit/<int:pk>/', ServiceUpdateView.as_view(), name='edit'),
    path('contact/', contacts, name='contact'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete'),
    path('product/<int:pk>/', cache_page(60)(ServiceDetailView.as_view()), name='product_detail'), ]
