from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect

from Packages.models import Package


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class PackageSelectView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		return render_to_response('packageselect.html', RequestContext(request))

		
		




