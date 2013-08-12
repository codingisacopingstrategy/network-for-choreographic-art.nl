import os, sys
sys.path.append('/home/s/apps/test.network-for-choreographic-art.nl/src')
sys.path.append('/home/s/apps/test.network-for-choreographic-art.nl/src/test.network-for-choreographic-art.nl')
os.environ['DJANGO_SETTINGS_MODULE'] = 'network_for_choreographic_art.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()