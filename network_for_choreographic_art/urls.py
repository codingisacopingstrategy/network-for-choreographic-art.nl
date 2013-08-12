from django.conf.urls.defaults import patterns, include, url
from network_for_choreographic_art.forms import LoginForm
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'network_for_choreographic_art.views.home', name='home'),
    url(r'^texts/proposal/$', 'network_for_choreographic_art.texts.views.proposal', name='proposal'),
    url(r'^texts/(?P<slug>[-\w]+)$', 'network_for_choreographic_art.texts.views.text', name='text'),    
    url(r'^proposal/sign/$', 'network_for_choreographic_art.views.sign', name='sign'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^login$', 'django.contrib.auth.views.login', {'authentication_form': LoginForm}, 'login'),
    url(r'^sign-up$', 'network_for_choreographic_art.views.sign_up', name='sign_up'),
    url(r'^password-reset$', 'django.contrib.auth.views.password_reset', {'from_email': 'Network for Choreography & Related Art <contact@network-for-choreographic-art.nl>'}),
    url(r'^password-reset/done$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^sign-up-successful$', 'network_for_choreographic_art.views.sign_up_success', name='sign_up_success'),
    url(r'^events/$', 'network_for_choreographic_art.events.views.index', name='events'),
    url(r'^events/info$', 'network_for_choreographic_art.events.views.info', name='events-info'),
    url(r'^events/(?P<slug>[-\w]+)$', 'network_for_choreographic_art.events.views.event'),
    url(r'^events/(?P<slug>[-\w]+)/join$', 'network_for_choreographic_art.events.views.join'),
    url(r'^events/(?P<slug>[-\w]+)/organise$', 'network_for_choreographic_art.events.views.organise'),
    url(r'^all-emails$', 'network_for_choreographic_art.views.all_emails', name='all_emails'),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^comments2/post$', 'network_for_choreographic_art.comments.post_comment'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
