from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login.models import User
from . models import Job
############################# HANDY HELPER #############################

def mainpage(request):
    context={
        "Job": Job.objects.all(),
        "User": User.objects.all()
    }
#bring in models
    
    return render(request,'handyhelper/mainpage.html',context)


############################# CREATE JOB #############################


def addjob(request):

    return render(request,'handyhelper/addjob.html')

def createjob(request):
    if request.method == 'POST':
        errors = Job.objects.job_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect ('/handyhelper/addjob')
        else:
            Job.objects.create(
                user = User.objects.get(id=request.session['userid']),
                title = request.POST['title'],
                desc = request.POST['desc'],
                location = request.POST['location'],
            )
        return redirect('/handyhelper/mainpage')

######################### VIEW JOB ###################

def viewjob(request,id):
    context={
        'job':Job.objects.get(id=id)
    }
    return render(request,'handyhelper/viewjob.html',context)

# def deletebooks(request,id):
#     Book.objects.filter(id=id).delete()
#     return redirect('/reads/main_page')

######################### EDIT JOB ###################

def editjob(request,id):
    context={
        'job':Job.objects.get(id=id)
    }
    return render(request,'handyhelper/editjob.html',context)

def edit(request,id):
    if request.method == 'POST':
        errors = Job.objects.job_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/handyhelper/editjob/'+id)
        else:
            edit = Job.objects.get(id=id)
           
            edit.title = request.POST['title'],
            edit.desc = request.POST['desc'],
            edit.location = request.POST['location'],
            edit.save()
            print ('edit')
    return redirect('/handyhelper/mainpage')



# ############################# LOGOUT #############################

def logout(request):
     request.session.clear()
    
     return redirect('/')

# ############################# DELETE Job #############################

def deletejob(request,id):
    delete=Job.objects.get(id=id)
    delete.delete()
    return redirect('/handyhelper/mainpage')