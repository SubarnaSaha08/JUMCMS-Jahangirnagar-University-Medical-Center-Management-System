from unittest.mock import patch

from django.http import HttpResponse
from django.test import TestCase, Client
from django.urls import reverse

from appointments.models import DoctorAppointment
from medicines.constants import MEDICINE_FREQUENCY_CHOICES
from medicines.models import Medicine, Prescription, PrescribedMedicine
from users.models import User, Doctor, Patient


class StorekeeperControllerTest(TestCase):
    """
    StroreKeeperControllerTest
    """

    def setUp(self):
        """
        Setup
        :return: Object
        """
        Medicine.objects.all().delete()
        Prescription.objects.all().delete()
        PrescribedMedicine.objects.all().delete()
        DoctorAppointment.objects.all().delete()
        User.objects.all().delete()
        Doctor.objects.all().delete()
        Patient.objects.all().delete()
        self.storekeeper_user = User.objects.create_user(
                email='storekeeper@example.com', name='Storekeeper', role='Storekeeper',
                blood_group='A+', date_of_birth='1980-01-01', gender='Male',
                phone_number='+8801712345678', password='asdf1234@'
                )
        self.doctor_user = User.objects.create_user(
                email='doctor@example.com', name='Dr. Sudipta', role='Doctor',
                blood_group='A+', date_of_birth='1980-01-01', gender='Male',
                phone_number='+8801712345678', password='asdf1234@'
                )
        self.patient_user = User.objects.create_user(
                email='patient@example.com', name='John Doe', role='Student',
                blood_group='B+', date_of_birth='1990-05-10', gender='Male',
                phone_number='+8801987654321', password='asdf1234@'
                )

        # Create doctor and patient instances
        self.doctor = Doctor.objects.create(user=self.doctor_user)
        self.patient = Patient.objects.create(user=self.patient_user)

        # Create appointment
        self.appointment = DoctorAppointment.objects.create(
                doctor=self.doctor, patient=self.patient,
                appointment_date_time='2024-12-15T10:00:00Z', status='scheduled'
                )

        # Create medicine
        self.medicine = Medicine.objects.create(
                name="Paracetamol", generic_name="Acetaminophen", manufacturer="ABC Pharma",
                dosage_form="Tablet", strength="500mg", description="Pain reliever",
                price=10.00, stock_quantity=100, expiry_date="2025-12-31"
                )

        # Create prescription and prescribed medicine
        self.prescription = Prescription.objects.create(
                doctor_appointment=self.appointment, diagnosis="Headache", next_visit_date='2024-12-22'
                )
        self.prescribed_medicine = PrescribedMedicine.objects.create(
                prescription=self.prescription, medicine=self.medicine,
                frequency=MEDICINE_FREQUENCY_CHOICES[0][0], duration=5, instructions="Take after meal"
                )

        # Create a client
        self.client = Client()

    def test_all_prescriptions_view(self):
        """
        All Prescriptions
        :return: Boolean
        """
        self.client.force_login(self.storekeeper_user)
        response = self.client.get(reverse('medicines:all_prescriptions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'storekeeper/prescription_list.html')
        self.assertIn('prescriptions', response.context)

    def test_search_prescriptions_view_get(self):
        """
        test_search_prescriptions_view_get
        :return: Boolean
        """
        self.client.force_login(self.storekeeper_user)
        response = self.client.get(reverse('medicines:search-prescriptions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'storekeeper/prescription_search.html')

    def test_search_prescriptions_view_post(self):
        """
        Test search_prescriptions_view_post
        :return:  Boolean
        """
        self.client.force_login(self.storekeeper_user)
        response = self.client.post(reverse('medicines:search-prescriptions'), {'patient_name': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'storekeeper/prescription_list.html')
        self.assertIn('prescriptions', response.context)
        self.assertEqual(len(response.context['prescriptions']), 1)

    def test_prescription_details_view(self):
        """
        test_prescription_details_view
        :return: Boolean
        """
        self.client.force_login(self.storekeeper_user)
        response = self.client.get(reverse('medicines:prescription-details', args=[self.prescription.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'storekeeper/prescribed_medicine_details.html')
        self.assertIn('prescription', response.context)
        self.assertIn('medicines_info', response.context)

    @patch('medicines.controllers.generate_pdf')  # Mock the generate_pdf function
    def test_dispense_medicines_view_success(self, mock_generate_pdf):
        """
        Test dispense_medicines_view_success
        :param mock_generate_pdf:
        :return:
        """
        mock_generate_pdf.return_value = HttpResponse()  # Mock the return value

        self.client.force_login(self.storekeeper_user)
        response = self.client.post(reverse('medicines:dispense-medicines', args=[self.prescription.id]))

        # Assert that the medicine stock quantity is updated
        updated_medicine = Medicine.objects.get(id=self.medicine.id)
        self.assertEqual(updated_medicine.stock_quantity, 95)

        # Assert that the response is a redirect (since generate_pdf is mocked)
        self.assertEqual(response.status_code, 200)

    def test_dispense_medicines_view_not_enough_stock(self):
        """
        test dispense medicines view_not_enough_stock
        :return: Boolean
        """
        self.client.force_login(self.storekeeper_user)
        self.medicine.stock_quantity = 2
        self.medicine.save()
        response = self.client.post(reverse('medicines:dispense-medicines', args=[self.prescription.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('medicines:search-prescriptions'))

    def test_add_medicine_controller(self):
        """
        Test add_medicine_controller

        """
        self.client.force_login(self.storekeeper_user)
        self.assertEqual(Medicine.objects.count(), 1)
        response = self.client.post(reverse('medicines:add-medicine'),
                                    {
                                        'name': "Capa",
                                        'generic_name': "Maracetamol",
                                        'manufacturer': "Square",
                                        'dosage_form': "Tablet",
                                        'strength': "200mg",
                                        'description': "Used for fever",
                                        'price': 10.00,
                                        'stock_quantity': 100,
                                        'expiry_date': "2025-12-31"
                                    },
                                    follow=False
                                    )
        self.assertRedirects(response,reverse('users:storekeeper_dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Medicine.objects.count(),2)
        self.assertEqual(Medicine.objects.first().name, "Paracetamol")
        self.assertEqual(Medicine.objects.first().generic_name, "Acetaminophen")
        self.assertEqual(Medicine.objects.first().manufacturer, "ABC Pharma")
        self.assertEqual(Medicine.objects.first().dosage_form, "Tablet")
        self.assertEqual(Medicine.objects.first().strength, "500mg")
        self.assertEqual(Medicine.objects.first().description, "Pain reliever")
        self.assertEqual(Medicine.objects.first().price, 10.00)
        self.assertEqual(Medicine.objects.first().stock_quantity, 100)
        self.assertEqual(str(Medicine.objects.first().expiry_date), "2025-12-31")