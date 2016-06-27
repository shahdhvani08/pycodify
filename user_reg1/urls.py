"""
Definition of urls for user_reg1.
"""

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from firstapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', user_reg1.views.home, name='home'),
    # url(r'^user_reg1/', include('user_reg1.user_reg1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', views.home),
    #url(r'^course/', views.course),
    url(r'^python_course/', include('firstapp.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login1/$', views.login1, name='login1'),
    # url(r'^intro/', 'firstapp.views.intro'),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
