from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm
from django.contrib import messages

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


