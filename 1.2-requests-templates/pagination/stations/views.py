import csv
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    page_number = int(request.GET.get("page",1))
    with open (settings.BUS_STATION_CSV, "r", encoding='utf-8', newline ='') as file:
        data = csv.DictReader(file)
        list = []
        for row in data:
            list += [row]
        paginator = Paginator(list,10)
        page = paginator.get_page(page_number)
        stations = []
        for row in page:
            stations += [row]
        context = {}
        context['bus_stations'] = stations
        context['page'] = page
    return render(request, 'stations/index.html', context)