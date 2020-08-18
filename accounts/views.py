from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import Login, Register, Profile, Mess, Student
from .models import Messfeedback
from django.http import HttpResponse

def register(request):


    if request.method == 'POST':
        reg = Register(request.POST)
        if reg.is_valid():

            first_name = reg.cleaned_data['first_name']
            last_name = reg.cleaned_data['last_name']
            username = reg.cleaned_data['username']
            email = reg.cleaned_data['email']
            password1 = reg.cleaned_data['password1']
            password2 = reg.cleaned_data['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username taken')
                    messages.info(request,'Please use different Username')
                    return redirect('/register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email registered with another account')
                    messages.info(request,'Please use a different Email address')
                    return redirect('/register')
                else:

                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=
                    password1)

                    user.save();
                    messages.info(request, 'registration successful')
                    return redirect('/register')
            else:
                messages.info(request, 'Password not matching')
                return redirect('/register')
    else:
        reg = Register()
        return render(request, 'register3.html', {'register':reg})
def login(request):
    lg
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')

    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")
def login1(request):
    if request.method == 'POST':
        lg = Login(request.POST)
        if lg.is_valid():

            username = lg.cleaned_data['username']
            password = lg.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('/login1')


    else:
        lg = Login()
        return render(request, 'login3.html', {'login': lg})




def student(request):
    st = Student()
    return render(request, 'student.html', {'student':st})

def mess(request):
        if request.method == 'POST':
            mf = Mess(request.POST)
            if mf.is_valid():
                ml = mf.cleaned_data['meal']
                rat = mf.cleaned_data['rating']
                rw = mf.cleaned_data['review']
                mes = Messfeedback(meal=ml, rating=rat, review=rw)
                mes.save()
                messages.info(request, 'feedback submitted')
                return redirect('/MessFeedback')
        else:
            mf = Mess()
            reviews = Messfeedback.objects.all()
            return render(request, 'messfeedback1.html', {'messfood':mf, 'revs':reviews})


