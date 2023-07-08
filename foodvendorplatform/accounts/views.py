from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm
from django.contrib import messages
from vendor.forms import RestaurantForm
from accounts.models import UserProfile
# Create your views here.


def registerUser(request):

    if request.method == 'POST':
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