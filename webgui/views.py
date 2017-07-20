from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
import locale
import datetime
from time import strftime
# from webgui.models import *


def homepage(request):
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    currentdate = datetime.date.today()
    birthdate = datetime.date(1989, 9, 17)
    nb_days = currentdate - birthdate
    nb_days = nb_days/365
    age = str(nb_days).split(" ")
    age = age[0]

    clock = strftime("%H:%M:%S")

    return render(request, 'homepage.html', {'clock': clock,
                                             'date': currentdate})

# def pro_experiences(request):
#     try:
#         experiences_list = Experience.objects.all()
#         for experience in experiences_list:
#             locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
#             experience.start_date = experience.start_date.strftime("%B %Y")
#             experience.end_date = experience.end_date.strftime("%B %Y")
#     except Experience.DoesNotExist:
#         experiences_list = None
#     return render(request, 'pro_experiences.html', {'experiences_list': experiences_list})
