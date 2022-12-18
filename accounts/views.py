from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname'] #same name as given as the form 
        last_name=request.POST['lastname']
        user_name=request.POST['username']
        email=request.POST['email']
        pass_word=request.POST['password']
        repass_word=request.POST['repassword']
        if pass_word==repass_word:
            if User.objects.filter(username=user_name):
                messages.info(request,"username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,"email is already taken")
                return redirect('register')  
            else:
                user=User.objects.create_user(username=user_name,password=pass_word,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
        else:
            print("Password is not macthed")
            messages.info(request,"Password is not macthed")  
            return redirect('register')  
        return redirect('/')
    else:
        return render(request, "registation.html")
