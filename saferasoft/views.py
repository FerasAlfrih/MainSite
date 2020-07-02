from django.shortcuts import render
from django.http import HttpResponseNotFound


def Er404(request, exception=None):
    return HttpResponseNotFound(request, exception, template_name='404.html')


def soon(request):
    return render(request, 'underconstraction.html')
