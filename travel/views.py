from django.http import HttpResponse
from django.shortcuts import render
from . models import place


# Create your views here.
# def fun(request):
#     # return HttpResponse("Hello Akhil")#to display a sepecific msg
#     return render(request, "home.html", {'name': 'Addition'})  # to display a html page

def fun(request):
    obj={'dept':place.objects.all()}
    # obj=place()
    # obj.name="python"
    # obj.desc="python  developer"
    return render(request,"index.html",obj)





def addition(request):
    number=int(request.POST["num1"])
    num=int(request.POST["num2"])
    num3=number+num
    return render(request, "result.html",{"add":num3})
