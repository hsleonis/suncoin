from django.shortcuts import HttpResponseRedirect
#from employee.models import UserProfile

class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith('/dashboard') and request.user.is_anonymous():
            return HttpResponseRedirect('/login')

        return response