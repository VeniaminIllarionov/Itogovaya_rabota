from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json
from doctors.models import Doctor
from services.models import Service, Record, Diagnostic
from users.models import User


class TestService(TestCase):
    """ Тестирование сервиса """

    def setUp(self):
        self.service = Service.objects.create(name="TEST1",
                                              description="Магнитно-резонансная томография (МРТ)",
                                              price=10000.00)
        self.user = User.objects.create(email='testuser@example.com', password='test123')
        self.doctor = Doctor.objects.create(name="Сергей",
                                            surname="Ватажко",
                                            patronymic="Борисович",
                                            work_experience=10,
                                            specialization="Врач общей практики",
                                            science="Врач высшей категории",
                                            post="Врач", )
        self.record = Record.objects.create(user=self.user,
                                            service=self.service,
                                            doctor=self.doctor,
                                            record_time="2024-08-23")
        self.diagnostic = Diagnostic.objects.create(user=self.user,
                                                    record=self.record,
                                                    result="Test",
                                                    diagnose="Test_diagnose"
                                                    )
        self.client = Client()
        self.list_url = reverse('services:home')
        self.detail_url = reverse('services:service_detail', args=[self.service.pk])
        self.delete_url = reverse('services:delete', args=[self.service.pk])



    def test_service_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'services/home.html')

    def test_service_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_service_delete_GET(self):
        response = self.client.delete(reverse(self.detail_url))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTemplateUsed(response, 'services/service_confirm_delete.html')



