from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
############################# LOGIN #############################

def index(request):
    context = {
        "User":User.objects.all()
    }
    return render(request,'login/index.html',context)

############################# CREATE USER #############################

def create(request):
    if request.method == "POST": 
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect ('/')
        else:
            userid=User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    password = request.POST['password']
                    )
            request.session['userid']=userid.id
            request.session['fname'] = userid.fname

            return redirect('/handyhelper/mainpage')
    # return redirect('/reads/main_page')

############################# LOGIN #############################

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect ('/')
        else:
            userid=User.objects.get(email = request.POST['logemail'])
            request.session['userid']=userid.id
            request.session['fname'] = userid.fname

            return redirect('/handyhelper/mainpage')

############################# LOGOUT #############################

def logout(request):
    request.session.clear()
    
    return redirect('/')

############################# DELETE USER #############################
def delete(request,id):
    delete=User.objects.get(id=id)
    delete.delete()
    
    return redirect('/')