from django.shortcuts import render


def Er404(request, exception=None):
    return HttpResponseNotFound(request, exception, template_name='404.html')
