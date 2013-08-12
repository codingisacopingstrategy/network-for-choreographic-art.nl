from django.contrib.auth.models import User, check_password
from django.template.defaultfilters import slugify

def full_to_split(full_name):
    name = full_name.split()
    if len(name) == 1:
        name.append(' ')
    if len(name) > 2:
        newname = [' '.join(name[0:-1])]
        newname.append(name[-1])
        name = newname
    return name

class EmailAuthBackend(object):
    """
    Email Authentication Backend
    
    Allows a user to sign in using an email/password pair rather than
    a username/password pair.
    """
    
    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
          
    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
