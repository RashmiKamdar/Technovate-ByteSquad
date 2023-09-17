# views.py

from django.shortcuts import render, redirect
from .models import DestinationTable
from Login.models import UserModel

def move_data(request):
    if request.method == 'POST':
        # Retrieve data from the SourceTable
        source_data = UserModel.objects.all()
        
        # Create new records in the DestinationTable based on the source data
        for source_record in source_data:
            DestinationTable.objects.create(
                Username=source_record.Username,
                Password=source_record.Password,
                FullName=source_record.FullName,
                Age=source_record.Age,
                Gender=source_record.Gender,
                Height=source_record.Height,
                Weight=source_record.Weight,
                BloodGroup=source_record.BloodGroup,
                OrganToDonate=source_record.OrganToDonate,
                MedicalHistory=source_record.MedicalHistory,
                Image=source_record.Image,
                Status=source_record.Status,
            )
        
        # Optionally, delete the records from the SourceTable
        source_data.delete()
        
        return redirect('success_page')  # Redirect to a success page after data transfer
    
    return render(request, 'toggle.html')
