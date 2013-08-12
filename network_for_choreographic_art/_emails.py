from django.contrib.auth.models import User
users = User.objects.all()

for user in users:
    if user.email != 'unknown' and '@' in user.email:
        print "%s <%s>," % (user.get_full_name(), user.email),