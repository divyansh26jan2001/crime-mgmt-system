from django.shortcuts import render,HttpResponse
from crime_mgmt.models import my_user,police_station, police, crime_category, criminal,fir
import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request,type):
    db = my_user.objects.all()
    name = ""
    if type == 'user':
        name = "Email"
    elif type == 'police':
        name = "Police ID"
    else:
        name = "Username"
    data = {
        'user_type' : type,
        'user_name' : name
    }

    try:
        if request.method == "POST":
            user_name = request.POST.get('email')
            password = request.POST.get('password')
            print(type,user_name,password)
            for i in db:
                if i.user_type==type and i.user_name == user_name and i.password == password:
                    data ={
                        'info' : i
                    }
                    if type == 'admin':
                        return render(request,'admin_dashboard.html',data)
                    elif type == 'police':
                        return render(request,'police_dashboard.html',data)
                    elif type == 'user':
                        return render(request,'user_dashboard.html',data)
                    break
            

    except:
        pass
    return render(request,'login.html',data)


# <! -------------------------------------------- ADMIN Panel ----------------------------------------------------------------------->
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def police_dashboard(request):
    return render(request,'police_dashboard.html')

def user_dashboard(request):
    return render(request,'user_dashboard.html')


# Police station views pages
def add_police_station(request):
    dt = police_station.objects.all()
    try:
        if request.method == "POST":
            station_name = request.POST.get('police_station_name')
            station_code = request.POST.get('police_station_code')
            d = datetime.datetime.now()
            for i in dt:
                if i.police_station_code == station_code:
                    data = police_station.objects.filter(police_station_code = station_code).update(police_station_name = station_name)
                    data.save()
                else:
                    data = police_station.objects.create(police_station_name = station_name,police_station_code = station_code,creation_date = d)

            data.save()
    except:
        pass
    return render(request,'add_police_station.html')

def add_police_station_data(request,detail):
    detail = detail.split(" ")
    code = detail[0]
    name = detail[1]
    print(code,name)
    dict = {
        'code' : code,
        'name' : name
    }
    return render(request,'add_police_station.html',dict)

def manage_police_station(request):
    dt = police_station.objects.all()
    data = {
        'info' : dt
    }
    return render(request,'manage_police_station.html',data)


# Police views functions
def add_police(request):
    dict = {
            'content' : police_station.objects.all()
        }
    try:
        if request.method == "POST":
            station = request.POST.get('police_station_name')
            station = station.split(" ")
            station = station[0]
            police_id = request.POST.get('police_id')
            police_name = request.POST.get('police_name')
            mail = request.POST.get('police_email')
            mobile = request.POST.get('police_mobile')
            address = request.POST.get('police_address')
            password = request.POST.get('police_password')
            print(station, police_id, police_name, mail, mobile, address, password)
            id = police_station.objects.get(police_station_code = station)
            data1 = police.objects.create(police_station_code = id,police_id = police_id,name = police_name,email = mail,mobile_number = mobile,Address = address,password = password)
            data2 = my_user.objects.create(user_type = 'police', user_name = police_id, password = password)
            print(data1, data2)
            data1.save()
            data2.save()
    except:
        pass
    return render(request,'add_police.html',dict)

def add_police_data(request,details):
    dict = {

    }
    return render(request,'add_police.html',dict)

def manage_police(request):
    dt = police.objects.all()
    data = {
        'info' : dt
    }
    return render(request,'manage_police.html',data)

#Crime category views functions
def add_crime_category(request):
    try:
        if request.method == "POST":
            name = request.POST.get('crime_category_name')
            desc = request.POST.get('crime_category_desc')
            data = crime_category.objects.create(category_name = name, category_desc = desc)
            data.save()
    except:
        pass
    return render(request,'add_crime_category.html')

def manage_crime_category(request):
    dt = crime_category.objects.all()
    data = {
        'info' : dt
    }
    return render(request,'manage_crime_category.html',data)

def update_crime_category(request):
    return render(request,'update_crime_category.html')


# <! ---------------------------------------------------------- POLICE Panel -------------------------------------------------------!>

# Criminal view function
id=0
def add_criminals(request):
    dict = {
        'st' : police_station.objects.all(),
        'ty' : crime_category.objects.all()
    }
    
    try:
        if request.method == "POST":
            station = request.POST.get('police_station_name')
            type = request.POST.get('crime_type')
            date =request.POST.get('crime_date')
            time = request.POST.get('crime_time')
            prison = request.POST.get('prison')
            court = request.POST.get('court')
            name = request.POST.get('criminal_name')
            number = request.POST.get('criminal_number')
            height = request.POST.get('criminal_height')
            weight = request.POST.get('criminal_weight')
            dob = request.POST.get('criminal_dob')
            email = request.POST.get('criminal_email')
            address = request.POST.get('criminal_address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            pincode = request.POST.get('pincode')
            id += 1
            
            photo = request.POST.get('photo')
            print(station,type,date,time,prison,court,name,number,height,weight,dob,email,address,city,state,country,pincode,photo)

            data = criminal.objects.create(police_station = station, crime_type = type, date=date, time=time, prison=prison, court=court, id=id, name=name, number=number, height=height, weight=weight, dob=dob, email=email, address=address, city=city, state=state, country=country, pincode=pincode, photo=photo)
            data.save()
    except:
        pass
    return render(request,'add_criminal.html',dict)

def manage_criminals(request):
    dt = criminal.objects.all()
    data = {
        'info' : dt
    }
    return render(request,'manage_criminal.html',data)

a=1
def update_criminals(request,type):
    dict = {
        'st' : police_station.objects.all(),
        'ty' : crime_category.objects.all(),
    }
    type = type.split(" ")[0]
    print(type)
    data = criminal.objects.all()
    for i in data:
        if i.id == type:
            dict['info'] = i
            return render(request,'update_criminal.html',dict)
    
    try:
        if request.method =="POST":
            station = request.POST.get('police_station_name')
            type = request.POST.get('crime_type')
            date =request.POST.get('crime_date')
            time = request.POST.get('crime_time')
            prison = request.POST.get('prison')
            court = request.POST.get('court')
            name = request.POST.get('criminal_name')
            number = request.POST.get('criminal_number')
            height = request.POST.get('criminal_height')
            weight = request.POST.get('criminal_weight')
            dob = request.POST.get('criminal_dob')
            email = request.POST.get('criminal_email')
            address = request.POST.get('criminal_address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            pincode = request.POST.get('pincode')
            photo=request.POST.get('photo')
            a=request.POST.get('criminal_id')

            for i in data:
                if i.id == a:
                    data = criminal.objects.filter(id = a).update(police_station = station, crime_type = type, date=date, time=time, prison=prison, court=court,name=name, number=number, height=height, weight=weight, dob=dob, email=email, address=address, city=city, state=state, country=country, pincode=pincode, photo=photo)
                    data.save()
                    break

    except:
        pass

def police_fir(request):
    dict = {
        
    }
    data = fir.objects.all()
    for i in data:
        if i.FIR_no == 'cyber123NDLPA':
            dict['info'] = i
    return render(request,'police_fir.html',dict)

def police_chargesheet(request):
    dict = {
        
    }
    data = fir.objects.all()
    for i in data:
        if i.FIR_no == 'cyber123NDLPA':
            dict['info'] = i
    return render(request,'police_chargesheet.html',dict)

# <!----------------------------------------- USER Panel -------------------------------------------------------------->
# FIR
def fir_form(request):
    dict = {
        'st' : police_station.objects.all(),
        'ct' : crime_category.objects.all()
    }

    try:
        if request.method == "POST":
            station = request.POST.get('police_station_name')
            type = request.POST.get('crime_type')
            accussed = request.POST.get('accussed_name')
            applicant = request.POST.get('applicant_name')
            parentage = request.POST.get('parentage')
            mobile = request.POST.get('applicant_mobile')
            address = request.POST.get('applicant_address')
            relation = request.POST.get('relation')
            purpose = request.POST.get('purpose')
            fir = type + station.split(" ")[0] + station.split(" ")[1]

            data = fir.objects.create(FIR_no = fir, police_station = station, crime_type = type, accused_name = accussed,applicant_name = applicant, parentage = parentage, number = mobile, address = address, relation_with_accussed = relation, purpose = purpose)
            data.save()

    except:
        pass
    return render(request,'fir_form.html',dict)

def fir_history(request):
    dict = {
        'info' : fir.objects.all()
    }
    return render(request,'fir_history.html',dict)

def fir_details(request):
    
    dict ={

    }
    data = fir.objects.all()
    for i in data:
        if i.FIR_no == 'cyber123NDLPA':
            dict['info'] = i
    
    return render(request,'fir_details.html',dict)

def user_chargesheet(request):
    
    dict = {
        
    }
    data = fir.objects.all()
    for i in data:
        if i.FIR_no == 'cyber123NDLPA':
            dict['info'] = i
    return render(request,'user_chargesheet.html',dict)