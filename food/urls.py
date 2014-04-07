from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from views import HomeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('Users.urls')),
    url(r'^packages/', include('Packages.urls')),
)
