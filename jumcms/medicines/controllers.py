from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Prescription, PrescribedMedicine


def search_prescriptions(request):
    """
    Allows lab technicians to search for prescriptions by patient name.
    """
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        prescriptions = Prescription.objects.filter(
            Q(doctor_appointment__patient__user__name__icontains=patient_name)
        ).order_by('-date_issued')
        context = {
            'prescriptions': prescriptions,
        }
        return render(request, 'lab_technician/prescription_list.html', context)
    else:
        return render(request, 'lab_technician/prescription_search.html')


def prescription_details(request, prescription_id):
    """
    Displays details of a specific prescription, including prescribed medicines.
    """
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    prescribed_medicines = PrescribedMedicine.objects.filter(prescription=prescription)
    context = {
        'prescription': prescription,
        'prescribed_medicines': prescribed_medicines,
    }
    return render(request, 'lab_technician/prescription_details.html', context)
# Create your views here.
