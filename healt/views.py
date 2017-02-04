from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
# Create your views here.
def home(request):

    return render(request,"base.html",{})

def dashboard(request):
    if request.user.is_authenticated():
        print ("hello")
        # if request.user.userProfile.exists():
        #     print ("profile exits")
        # else:
        #     print ("profile doesn't exits")
        if request.user.healthOfficer.exists():
            print ('officer')
            query = Query.objects.all()
            return render(request,"officer_dashboard.html",{
                'query':query
            })
        elif request.user.userProfile.exists():
            print ("user")
            query = Query.objects.filter(posted_by= request.user.userProfile.get())
            return render(request,"user_dashboard.html",{
                'query':query
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
        profile = UserProfile(
            user = request.user,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            city=city
        )
        profile.save()



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
            rum.save()
        return render(request,"rumour.html",{
            'rumour':rum
        })
        