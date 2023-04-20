from django.shortcuts import render,redirect
from home.models import ContactData,Product,Project
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')

def myClick(request):
    return render(request, 'myclick.html')

def myphoto(request):
    return render(request, 'me.html')

def project(request):
    return render(request, 'project.html',{'project':Project.objects.all()})

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        desc=request.POST.get('desc')
        if "" not in (name,email,subject,desc):
            try:
                contact=ContactData(name=name,email=email,subject=subject,desc=desc,date=datetime.today())
                contact.save()
                messages.success(request, "Message Sent !!!")
            except Exception as e:
                messages.warning(request, "Some Error Occured !!! Please try again")
        else:
            messages.add_message(request,messages.INFO,"Field Empty !!! Please fill the form")
            
    return render(request, 'contact.html')

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Login Successful")
            return redirect('/logged') 
        else:
             messages.warning(request, "Invalid Login Credentials")
    if not request.user.is_anonymous:
        return redirect('/logged')
    else:
        return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect("/")

def logged(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request, 'logged.html', {'products':Product.objects.all()})
    
def loggedsettings(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        if "" not in (email,firstname,lastname):
            user=User.objects.get(username=request.user)
            if email!=str(request.user):
                if not User.objects.filter(username=email).exists():
                    user.username=email
                    user.first_name=firstname
                    user.last_name=lastname
                    user.save()
                    messages.success(request, "Profile Updated !!!")
                    return redirect('/logged')
                else:
                    messages.warning(request, "Account already exists with this Email ID !!!")
            else:
                user.first_name=firstname
                user.last_name=lastname
                user.save()
                messages.success(request, "Profile Updated !!!")
                return redirect('/logged')
        else:
            messages.warning(request, "Field Empty !!! Please fill the necessary details")

    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'loggedsettings.html')

def signupPage(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        if "" not in (email,firstname,lastname,password,repassword):
            if User.objects.filter(username=email).exists():
                messages.warning(request, "Account already exists with this Email ID !!!")
            else:
                try:
                    if password==repassword:
                        user=User.objects.create_user(email,email,password)
                        user.email=email
                        user.first_name=firstname
                        user.last_name=lastname
                        user.save()
                        messages.success(request, "Account Created !!!Now you may Login")
                        return redirect('/login')
                    else:
                        messages.warning(request,"Passwords dosent match !!! Try again")    
                except Exception as e:
                    messages.warning(request, "Some Error Occured !!! Please try again")
        else:
            messages.add_message(request,messages.INFO,"Field Empty !!! Please fill the form")
    if not request.user.is_anonymous:
        return redirect('/logged')
    else:
        return render(request, 'signup.html')
    
def passwordChange(request):
    if request.method == 'POST':
        pre_pass=request.POST.get('prepassword')
        new_pass=request.POST.get('newpassword')
        renew_pass=request.POST.get('renewpassword')
        if new_pass==renew_pass:
            if authenticate(username=request.user,password=pre_pass)!=None:
                user=User.objects.get(username=request.user)
                user.set_password(new_pass)
                user.save()
                messages.success(request,"Password Changed Successfully !!!")
                return redirect('/logged')
            else:
                messages.warning(request,"Authentication Failed !!!")
        else:
            messages.warning(request, "Re-entered password dosen't match with new password")
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'loggedsettings.html')

def purchase(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request, 'purchase.html')