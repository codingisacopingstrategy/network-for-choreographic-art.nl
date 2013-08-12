from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django import forms

class SignUpForm(UserCreationForm):
    """ Require email address when a user signs up """
    email = forms.EmailField(label='Email address', max_length=75)
    
    """ Require first and last name """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name') 

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email address already exists. Did you forget your password?")
        except User.DoesNotExist:
            return email
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_active = True # change to false if using email activation
        if commit:
            user.save()
            
        return user

class LoginForm(AuthenticationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            raise forms.ValidationError("We could not find this user in the system. Have you signed up?")
        return username
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("The password you entered is incorrect. You can reset your password"))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))
        
        # TODO: determine whether this should move to its own method.
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))
        
        return self.cleaned_data


