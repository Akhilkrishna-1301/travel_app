from django.http import HttpResponse
from django.shortcuts import render
from . models import place


# Create your views here.
# def fun(request):
#     # return HttpResponse("Hello Akhil")#to display a sepecific msg
#     return render(request, "home.html", {'name': 'Addition'})  # to display a html page

def fun(request):
    obj={'dept':place.objects.all()}
    return render(request,"index.html",obj)


def detail(request,prod_id):
    product1={'product':place.objects.get(id=prod_id)}
    return render(request,"detail.html",product1)

    # product1=place.objects.get(id=prod_id)
    # return render(request,'detail.html',{'product':product1})

# def addition(request):
#     number=int(request.POST["num1"])
#     num=int(request.POST["num2"])
#     num3=number+num
#     return render(request, "result.html",{"add":num3})
