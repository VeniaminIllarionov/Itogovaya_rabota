from django.urls import path
from django.views.decorators.cache import cache_page

from services.apps import ServicesConfig
from services.views import (contacts, ServiceDetailView, ServiceListView, ServiceCreateView, ServiceUpdateView,
                            ServiceDeleteView, company, RecordCreateView, RecordListView, RecordDeleteView,
                            RecordUpdateView, DiagnosticListView)

app_name = ServicesConfig.name

urlpatterns = [
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('', ServiceListView.as_view(), name='home'),
    path('edit/<int:pk>/', ServiceUpdateView.as_view(), name='edit'),
    path('contact/', contacts, name='contact'),
    path('company/', company, name='company'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', cache_page(60)(ServiceDetailView.as_view()), name='service_detail'),
    path('record/', RecordCreateView.as_view(), name='record'),
    path('record/list/', RecordListView.as_view(), name='record_list'),
    path('record/delete/<int:pk>/', RecordDeleteView.as_view(), name='record_delete'),
    path('record/edit/<int:pk>/', RecordUpdateView.as_view(), name='record_edit'),
    path('diagnostic/', DiagnosticListView.as_view(), name='diagnostic_list'),]
