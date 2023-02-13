from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import auth
from .models import Profile 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
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
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request , 'Email Already Exist') 
                return redirect('signup')
            else :
                user = User.objects.create_user(username=username , email= email , password= password)
                user.save()

                # log the user in and redirect to settings page


                user_model = User.objects.get(username= username)
                new_profile = Profile.objects.create(user = user_model , id_user = user_model.id)
                new_profile.save()
                return redirect('/')
        else :
            messages.info(request , "Password not matching")
            return redirect('signup')
    else :
        return render(request , 'signup.html')
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

def signIn(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']

        user = auth.authenticate(username= username , password = password)

        if user is not None :
            auth.login(request , user)
            return redirect('home')
        else:
            messages.info(request , 'Credentials Invalid')
            return redirect('signin')
    else :
        return render(request , 'signin.html')    