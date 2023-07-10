from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm
from django.contrib import messages, auth
from vendor.forms import RestaurantForm
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from .utils import detect_user
from django.contrib.auth.decorators import user_passes_test
from .utils import check_role_customer, check_role_vendor
# Create your views here.




#      Register User View

def registerUser(request):

    if request.user.is_authenticated:
        messages.warning(request, "User already registered")
        return redirect('myAccount')

    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = 2
            user.save()
            messages.success(request, 'user saved successfully')

            return redirect('registerUser')
        else:
            print('no valid form')
            print(form.errors)

    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)



# register Restaurant View


def registerRestaurant(request):

  
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = RestaurantForm(request.POST, request.FILES)


        if form.is_valid() and v_form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = 1
            user.save()

            #  now creating restaurant instance 

            restaurant = v_form.save(commit=False)
            restaurant.user = user
            restaurant.user_profile = UserProfile.objects.get(user=user)
            restaurant.save()

            messages.success(request, "Account created. please wait for approval")

            return redirect('registerRestaurant')
        
        else:
            print(form.errors, v_form.errors)


    else:
        form = UserForm()
        v_form  = RestaurantForm()

    context = {'form': form, 'v_form': v_form}

    return render(request, 'accounts/register_restaurant.html', context)






# Login View

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "User already logged In")
        return redirect('myAccount')
    
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, email=email, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('myAccount')
        else:
            messages.error(request, 'credentials are not valid')
            return redirect('login')
    


    return render(request, 'accounts/login.html')


# Logout View

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successful')
    return redirect('login')


# myaccount detection 

@login_required(login_url='login')

def myAccount(request):
    user = request.user
    redirect_url = detect_user(user)
    return redirect(redirect_url)


# customer Dashboard  View
@login_required(login_url='login')
@user_passes_test(check_role_customer)
def custDashboard(request):
    return render(request, 'accounts/cust_dashboard.html')



# resturant Dashboard  View
@login_required(login_url='login')
@user_passes_test(check_role_vendor)

def restDashboard(request):

    return render(request, 'accounts/rest_dashboard.html')