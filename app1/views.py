from django.shortcuts import render
from django .http import HttpResponse
from .models import Employee, Department


def hello(request):
    return HttpResponse('start the hello in app1')

def first1_html(request):
    return render(request,'first1.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        title = request.POST['title']
        Experience = request.POST['Experience']
        data = Employee.objects.create(name=name,age=age,title=title,Experience=Experience)
        Department.objects.create(dept_name=request.POST['dept_name'],salary = request.POST['salary'],employee = data)
        return HttpResponse('data saved successfully')
    return render(request,'first_form.html')


def alldata(request):
    data = Employee.objects.all()
    print(data)
    return render(request,'alldata.html',{'data':data})

def singledata(request,name):
    data = Employee.objects.get(name=name)
    return render(request,'single_data.html',{'data':data})

def update(request,name):
    """metood1"""
    data = Employee.objects.get(name=name)
    if request.method == "POST":
        data.name = request.POST['name']
        data.age = request.POST['age']
        data.Experience = request.POST['Experience']
        data.title = request.POST['title']
        data.save()
        return HttpResponse('data updated successfully')

    # """method 2"""
    # data = Employee.objects.get(name=name)
    # if request.method == "POST":
    #     data_dict = dict(request.POST)
    #     print('dictionary is',data_dict)
    #     data_dict.pop('csrfmiddlewaretoken')
    #     data_dict = {j: data_dict[j][0] for j in data_dict.keys()}
    #
    #     filter_dict = Employee.objects.filter(name=name)
    #     filter_dict.update(**data_dict)
    #     return HttpResponse('data updated successfully')
    return render(request,'update.html',{'data':data})


def delete(request,name):
    data = Employee.objects.get(name=name)
    data.delete()
    return HttpResponse('data deleted')