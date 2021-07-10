from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from .models import District, Village, Taluka,Farmer
from .function import handle_uploaded_file
from datetime import datetime
import csv  


def farmer_details(request):
    if request.method == 'POST':
        if 'd_id' in request.POST:
            photo = handle_uploaded_file(request.FILES['photo']) 
            farmer =  Farmer()
            farmer.first_name = request.POST.get('f_name')
            farmer.middle_name = request.POST.get('m_name')
            farmer.last_name = request.POST.get('l_name')
            farmer.mobile_number = request.POST.get('mob_no')
            farmer.aadhaar_number = request.POST.get('a_no')
            farmer.district_id = request.POST.get('district')
            farmer.taluka_id = request.POST.get('taluka')
            farmer.village_id = request.POST.get('village_ids1')
            farmer.address = request.POST.get('address')
            farmer.img_path = photo
            farmer.added_on = datetime.now()
            farmer.farmer_active = True
            farmer.save()
            return redirect('farmer_details')
        elif 'd_id1' in request.POST:
            farmer = Farmer.objects.get(id=request.POST.get('d_id1'))
            if request.FILES:
                photo = handle_uploaded_file(request.FILES['photo1']) 
                farmer.img_path = photo
            farmer.first_name = request.POST.get('f_name1')
            farmer.middle_name = request.POST.get('m_name1')
            farmer.last_name = request.POST.get('l_name1')
            farmer.mobile_number = request.POST.get('mob_no1')
            farmer.aadhaar_number = request.POST.get('a_no1')
            farmer.address = request.POST.get('address1')
            farmer.save()
            return redirect('farmer_details')
        else:
            return redirect('farmer_details')
    else:
        district_data = list(District.objects.values())
        farmer_data = Farmer.objects.all()
        return render(request, 'farmer_details.html',{'district_data':district_data, 'farmer_data':farmer_data})


def district(request):
    if request.is_ajax():
        id = request.POST.get('id')
        data = Taluka.objects.filter(district_id_id=id)
        lst_taluka = list(data.values())
        return JsonResponse({'taluka':lst_taluka})


def taluka(request):
    if request.is_ajax():
        id = request.POST.get('id')
        data = Village.objects.filter(taluka_id_id=id)
        lst_village = list(data.values())
        return JsonResponse({'village':lst_village})


def frm_cnt(request):
    if request.is_ajax():
        id = request.POST.get('id')
        data = Farmer.objects.filter(village_id=id).count()
        return JsonResponse({'data':data})


def report(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    farmer = Farmer.objects.all()  
    writer = csv.writer(response)  
    writer.writerow(['ID','First Name','Last Name', 'Mobile Number','Adadhaar Number'])
    for farm in farmer:  
        writer.writerow([farm.id,farm.first_name,farm.last_name, farm.mobile_number, farm.aadhaar_number])  
    return response  
