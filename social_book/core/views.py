from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from .models import Profile 
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def signUp(request):

    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        password2 = request.POST['Password2'] 

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request ,'Username taken!') 
                return redirect('signUp')
            elif User.objects.filter(email=email).exists():
                messages.info(request , 'Email Already Exist') 
                return redirect('signUp')
            else :
                user = User.objects.create_user(username=username , email= email , password= password)
                user.save()

                # log the user in and redirect to settings page


                user_model = User.objects.get(username= username)
                new_profile = Profile.objects.create(user = user_model , id_user = user_model.id)
                new_profile.save()
                return redirect('signUp')
        else :
            messages.info(request , "Password not matching")
            return redirect('signUp')
    else :
        return render(request , 'signup.html')