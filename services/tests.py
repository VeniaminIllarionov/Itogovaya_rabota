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
        self.user = User.objects.create(email='testuser@example.com')
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
        self.create_url = reverse('services:create')
        self.detail_url = reverse('services:service_detail', args=[self.service.pk])

    def test_create_service(self):
        """ Тестирование создания сервиса """

        response = self.client.get(self.create_url, {"name": "TEST2",
                                                     "description": "МРТ",
                                                     "price": '12000.00', })

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Service.objects.all().count(), 1)
        self.assertEqual(HttpResponseRedirect, 'TEST2')
        # self.assertEqual(data.get("course"), self.lesson.course.id)

        # self.assertEqual(data.get("url_video"), "https://www.youtube.com/watch")
        # self.assertEqual(data.get("description"), "Test")

    def test_service_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'services/home.html')

    def test_service_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_service(self):
        """ Тестирование удаления сервиса """

        url = reverse("services:delete", args=(self.service.pk,))
        data = {
            "name": "TEST1",
            "description": "Магнитно-резонансная томография (МРТ)",
            "price": '10000.00',
        }

        response = self.client.delete(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_service(self):
        """ Тестирование изменения сервиса """

        url = reverse("services:edit", args=(self.service.pk,))
        data = {
            "name": "TEST2",
            "description": "МРТ",
            "price": '12000.00',
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(data.get("name"), "TEST2")
        self.assertEqual(data.get("description"), "МРТ")
        self.assertEqual(data.get("price"), '12000.00')
