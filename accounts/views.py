from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
#log in page
   

#registration form
def register(request):
    
    if request.method=="POST":
        username=request.POST['username']#same name as given as the form 
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username):
                messages.info(request,"username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,"email is already taken")
                return redirect('register')  
            else:
                 user=User.objects.create_user(username=username,password=password1,email=email,)
                 user.save();
        else:
            print("password not matched")
            messages.info(request,"Password is not macthed")
            return redirect('register')          
        return render(request,'login.html')
    else:
         return render(request,'registation.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            
            return redirect('login')
    else:
        return render(request,"login.html")    
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    
    
    # if request.method=="POST":
    #     first_name=request.POST['firstname'] #same name as given as the form 
    #     last_name=request.POST['lastname']
    #     user_name=request.POST['username']
    #     email=request.POST['email']
    #     pass_word=request.POST['password']
    #     repass_word=request.POST['repassword']
    #     if pass_word==repass_word:
    #         if User.objects.filter(username=user_name):
    #             messages.info(request,"username is already taken")
    #             return redirect('register')
    #         elif User.objects.filter(email=email):
    #             messages.info(request,"email is already taken")
    #             return redirect('register')  
    #         else:
    #             user=User.objects.create_user(username=user_name,password=pass_word,email=email,first_name=first_name,last_name=last_name)
    #             user.save();
    #             print("user created")
    #     else:
    #         print("Password is not macthed")
    #         messages.info(request,"Password is not macthed")  
    #         return redirect('register')  
    #     return redirect('/')
    # else:
    #     return render(request, "registation.html")
