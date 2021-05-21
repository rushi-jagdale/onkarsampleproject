from django.shortcuts import render
from django .http import HttpResponse
from .models import survey

def hello2(request):
    return HttpResponse('you are in app2')
# Create your views here.

def register2(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        survey.objects.create(name=name,email=email,city=city)
        return HttpResponse('data saved successfully')
        # print(request.POST)
    return render(request,'register2.html')

def privacy(request):
    return render(request,'privacy.html')

def alldata2(request):
    data = survey.objects.all()
    return render(request,'alldata2.html',{'data':data})

def update2(request,name):
    data = survey.objects.get(name=name)
    if request.method == "POST":
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.city = request.POST['city']
        data.save()
        return HttpResponse('data saved successfully')
    return render(request,'update2.html',{'data':data})

def delete(request,name):
    data = survey.objects.get(name=name)
    data.delete()
    return HttpResponse('data deleted')
