from django.shortcuts import render,redirect
from django.http import HttpResponse
from app4.models import student
# Create your views here.
def home(request):
    return render(request, 'home.html')

def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def userpage(request):
    return render(request,'userpage.html')

def adminpage(request):
    return render(request,'adminpage.html')

def modify(request):
    operation=request.GET['operation']
    name=request.GET['name']
    username=request.GET['username']
    password=request.GET['password']
    gender=request.GET['gender']
    mobile=request.GET['mobile']
    email=request.GET['email']
    desig=request.GET['desig']
    course=request.GET['course']
    graduation=request.GET['graduation']
    address=request.GET['address']
    pincode=request.GET['pincode']
    r=student.objects.get(email=email)
    if operation=="update":
        r.name=name
        r.username=username
        r.password=password
        r.gender=gender
        r.mobile=mobile
        r.email=email
        r.desig=desig
        r.course=course
        r.graduation=graduation
        r.address=address
        r.pincode=pincode
        r.save()
    else:
        student.delete(r)
    users=student.objects.all()
    return render(request,'viewusers.html',{"users":users})

def viewusers(request):
    users=student.objects.all()
    return render(request,'viewusers.html',{"users":users})

def doregister(request):
    name=request.GET['name']
    username=request.GET['username']
    password=request.GET['password']
    gender=request.GET['gender']
    mobile=request.GET['mobile']
    email=request.GET['email']
    desig=request.GET['desig']
    course=request.GET['course']
    graduation=request.GET['graduation']
    address=request.GET['address']
    pincode=request.GET['pincode']


    r=student()
    r.name=name
    r.username=username
    r.password=password
    r.gender=gender
    r.mobile=mobile
    r.email=email
    r.desig=desig
    r.course=course
    r.graduation=graduation
    r.address=address
    r.pincode=pincode
    r.save()
    return render(request, 'login.html')

def logincheck(request):
    username=request.GET['uname']
    password=request.GET['pwd']
    r=None
    try:
        r=student.objects.get(username=username, password=password)
    except Exception as ex:
        return render(request, 'login.html',{"msg":"Invalid username or password"})
    if(r!=None):
        if(r.desig=='user'):
            return redirect('/userpage')
        if(r.desig=='admin'):
            return redirect('/adminpage')
        else:
            return render(request,"login.html",{"msg":"invalid designation"})
    return render(request, 'home.html')