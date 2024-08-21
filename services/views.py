from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from services.forms import ServiceForm
from services.models import Service
from users.services import get_qs_from_cache


class ServiceListView(ListView):
    model = Service
    template_name = 'services/home.html'

    def get_queryset(self):
        return get_qs_from_cache(qs=Service.objects.all(), key='service_list')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение: {name}({phone}): {message}')
    return render(request, 'services/contacts.html')


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"




class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('services:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'services/product_detail.html'
    login_url = "users:login"
    redirect_field_name = "redirect_to"



