from django import forms
from vendor.models import Vendor
from accounts.forms import UserForm
# start from here 


class RestaurantForm(forms.ModelForm):

    class Meta():
        model = Vendor
        fields = ['restuarant_name', 'restuarant_license']
        

