from django.urls import path
from . import views


urlpatterns = [
    path('', views.coInfo, name='CovUpdate'),
    # path('info/', views.search, name='results'),

]
