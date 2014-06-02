from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from views import HomeView, SuccessView, VegView, NonVegView, FitnessView, ComboRegistration

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'), 
    #url(r'^$', ComboRegistration.as_view(), name='registration_combo'),
    url(r'^after_register/', SuccessView.as_view(), name='after_register'),
    url(r'^veg/', VegView.as_view(), name='veg'),
    url(r'^nonveg/', NonVegView.as_view(), name='nonveg'),
    url(r'^fitness/', FitnessView.as_view(), name='fitness'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('Users.urls')),
    url(r'^packages/', include('Packages.urls')),
) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
