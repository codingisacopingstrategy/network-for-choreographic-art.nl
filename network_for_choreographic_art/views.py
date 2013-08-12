from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from random import shuffle
from petition.models import User, Vote
from django.contrib.auth.models import User as UserAuth
from photos import photos
from django.template.defaultfilters import slugify
from forms import SignUpForm
from network_for_choreographic_art.decorators import superuser_only

import datetime

def full_to_split(full_name):
    name = full_name.split()
    if len(name) == 1:
        name.append(' ')
    if len(name) > 2:
        newname = [' '.join(name[0:-1])]
        newname.append(name[-1])
        name = newname
    return name

def _photos():
    shuffle(photos)
    return photos[:6]

def home(request):
    petition = Vote.objects.all().order_by('-pub_date')
    return render_to_response('home.html',{'slug': 'home', 'petition': petition, 'count' : len(petition), 'photos': _photos()},context_instance=RequestContext(request))

def sign(request):
    p1 = User(full_name = request.POST['full_name'], email= request.POST['email'], function = request.POST['function'], join_date=datetime.datetime.now())
    p1.save()
    p2 = Vote(pub_date=datetime.datetime.now(),voter=p1)
    p2.save()
    return HttpResponseRedirect('/')

def sign_up(request):
    """ User sign up form """
    if request.method == 'POST':
        data = request.POST.copy() # so we can manipulate data

        # random username
        data['username'] = slugify(data['first_name'] + ' ' + data['last_name'])
        form = SignUpForm(data)
            
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/sign-up-successful')
    else:
        form = SignUpForm()

    return render_to_response('registration/sign-up.html', {'form':form},
                              context_instance=RequestContext(request))

def sign_up_success(request):
    return render_to_response('registration/sign-up-success.html', context_instance=RequestContext(request))

@superuser_only
def all_emails(request):
    users = UserAuth.objects.all()
    all_emails = ''
    for user in users:
        if user.is_active and user.email != 'unknown' and '@' in user.email:
            all_emails += "%s <%s>, " % (user.get_full_name(), user.email)
    return render_to_response('all_emails.html', { 'emails' : all_emails } ,context_instance=RequestContext(request))