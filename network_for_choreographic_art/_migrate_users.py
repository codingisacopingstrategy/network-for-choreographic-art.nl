from petition.models import User
from django.contrib.auth.models import User as UserO
from django.template.defaultfilters import slugify
from django.db.utils import IntegrityError

users = User.objects.all()

for user in users:
    try:
        username = slugify(user.full_name)
        #The goal is to have a list name: ['Eric Martijn', 'Schrijver']
        name = user.full_name.split()
        if len(name) == 1:
            name.append(' ')
        if len(name) > 2:
            newname = [' '.join(name[0:-1])]
            newname.append(name[-1])
            name = newname
        email = user.email
        if user.email == "":
            email = "unknown"
        u1 = UserO.objects.create_user(username, email, username)
        u1.first_name = name[0]
        u1.last_name = name[1]
        u1.save()
        print "created user %s" % u1.get_full_name()
    except IntegrityError:
        print "DUPLICATE %s" % user.full_name
