from django.shortcuts import render, HttpResponseNotFound


def Er404(request, exception=None):
    return HttpResponseNotFound(request, exception, template_name='404.html')
