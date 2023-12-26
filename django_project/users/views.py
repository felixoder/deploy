from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .form import RegisterCustomerForm

#register a customer

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.save()
            messages.info(request,'Your Account has been successfully Registered Please Log in to Continue')
            return redirect('login')

        else:
            messages.warning(request,'Something went wrong. Please Check the form input correctly')
            return redirect('register-customer')
    else:
        form = RegisterCustomerForm()
        context = {'form':form}
        return render(request , 'users/register_customer.html',context)



#login user

def login_user(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password= password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request,'Login Successfully. Please enjoy your session')
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong . Please check the form inputs')
            return redirect('login')

    else:
        return render(request,'users/login.html')

#logout a user

def logout_user(request):
    logout(request)
    messages.info(request,'Your session has ended. Please login to continue')
    return redirect('login')
    





