from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from crm.forms import SignUpForm


def index(request):
    return HttpResponse('Index Page.')


class SignUpView(generic.FormView):
    form_class = SignUpForm
    template_name = 'crm/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
