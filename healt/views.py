from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone

import unirest,requests


# Create your views here.
def home(request):

    return render(request,"index.html",{})

def profile(request):
    if request.user.is_authenticated() and request.user.userProfile.exists():
        userp = UserProfile.objects.get(user=request.user)
        c = City.objects.all()
        print (request.user)
        return render(request,"user_profile.html",{
        'userp':userp,
        'city':c
    })
    else:
        return redirect('/dashboard')


def dashboard(request):
    if request.user.is_authenticated():
        print ("hello")
        # if request.user.userProfile.exists():
        #     print ("profile exits")
        # else:
        #     print ("profile doesn't exits")
        if request.user.healthOfficer.exists():
            print ('officer')
            query = Query.objects.all().order_by('-posted_date', 'id')
            return render(request,"officer_dashboard.html",{
                'query':query
            })
        elif request.user.userProfile.exists():
            print ("user")
            query = Query.objects.filter(posted_by= request.user.userProfile.get()).order_by('-posted_date', 'id')
            otherq = Query.objects.exclude(posted_by= request.user.userProfile.get()).filter(status="Confirmed").order_by('-posted_date', 'id')
            return render(request,"user_dashboard.html",{
                'query':query,
                'otherq':otherq
            })
        else:
            # redirect to complete profile 
            return redirect('/profileComplete')
        # print (request.user.userProfile.get().first_name)
    else:
        print ("Bye")
    return render(request,"base.html",{})

# def addQuery(request):
#     if request.method==POST:
#         print ("metho post")
#     else
def profileComplete(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    if request.user.healthOfficer.exists() or request.user.userProfile.exists() :
        return redirect('/dashboard')   
    
    if request.method == 'POST':
        print ("hello")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        city_selected = request.POST.get("city_selected")
        city = request.POST.get("city")
        if city == "":
            city = city_selected
        else:
            a = City(name=city)
            a.save()
        profile = UserProfile(
            user = request.user,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            city=city
        )
        profile.save()

        return redirect('/dashboard')



    city = City.objects.all()


    return render(request,"profileComplete.html",{
        'city': city
    })


def addQuery(request):
    if request.user.is_authenticated() and request.method == 'POST':
        print ("hello")
        # print (request.POST.get("name"))
        print (request.POST)
        posted_by = UserProfile.objects.get(user = request.user)
        name = request.POST.get("name")
        number_of_affected = request.POST.get("affected_number")
        area_selected = request.POST.get("affected_area_select")
        area = request.POST.get("affected_area")
        affected_age_group = request.POST.get("affected_age_group")
        number_of_casuality = request.POST.get("casuality_number")
        if area == "":
            area = area_selected
        else:
            a = City(name=area)
            a.save()
        q = Query(
            posted_by= posted_by,
            name = name,
            number_of_affected = number_of_affected,
            number_of_casualties = number_of_casuality,
            status = 'Pending',
            affected_city = area,
            affected_age_group = affected_age_group,
        )
        print (q)
        q.save()
        return redirect('/dashboard')
    
    city = City.objects.all()
    print (city[0])
    return render(request,"addQuery.html",{
        'city':city
    })

def rumour(request,id):
        print (id)
        rum = Query.objects.get(id=id)
        if request.method == 'POST':
            print ( request.POST)
            if request.POST.get("verify"):
                rum.status = 'Confirmed'      
            else:
                rum.status = 'FalseAlarm'
            rum.verified_by = HealthOfficer.objects.get(user = request.user)
            rum.verified_date = timezone.now()
            rum.save()
        return render(request,"rumour.html",{
            'rumour':rum
        })
def send_message(sid, token, sms_from, sms_to, sms_body):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body
        })

def addPrecaution(request,id):
    q = Query.objects.get(id = id)

    sid = "hackhere"
    token = "e46a5589b3d69190ec34926022c4676495ab3bea"

    sms_from = "08039510254"
    sms_to = "08507118002"
    sms_body = "hi"
    r = send_message(sid,token,sms_from,sms_to,sms_body)
    print (r.status_code)

    if request.method == "POST":
        prec = request.POST.get("addPrecaution")
        q.precaution = prec
        q.save()

        return redirect('/dashboard')


    
    return render(request,"addPrecaution.html",{
        'q':q
    })

def viewRumour(requests,id):
    q = Query.objects.get(id=id)
    if not q.status == "Confirmed":
        return redirect("/")
    return render(requests,"viewRumour.html",{
        'q':q
    })
