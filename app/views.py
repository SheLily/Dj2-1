from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from urllib.parse import urlencode


with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
    reader = list(csv.DictReader(csvfile))


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = int(request.GET.get('page')) or 1
    params = urlencode({'page': current_page + 1})
    next_page_url = reverse('bus_stations') + '?' + str(params)

    return render(request, 'index.html', context={
        'bus_stations': reader[10 * current_page - 1: 10 * current_page + 10],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })
