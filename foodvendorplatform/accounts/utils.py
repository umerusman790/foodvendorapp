
from django.core.exceptions import PermissionDenied
# utility functions are defined in the following file


def detect_user(user):
    url = None
    if user.role == 1:
        url = 'restDashboard'
    elif user.role == 2:
        url = 'custDashboard'
    elif user.role == None and user.is_superuser:
        url = '/admin'

    return url



def check_role_vendor(user):
    if user.role == 1:
        return True
    else :
        raise PermissionDenied
    

def check_role_customer(user):
    if user.role == 2:
        return True
    else :
        raise PermissionDenied
    