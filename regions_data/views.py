import csv
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from .models import Region, District, Parse
from .forms import ParseForm, ShowForm


def show(request):
    form = ShowForm
    return render(request, 'regions_data/show.html', locals())


def select_region(request):
    if 'region_pk' in request.GET and request.GET.getlist('region_pk')[0] != '':
        region_pk = int(request.GET.getlist('region_pk')[0])

        districts_list = District.objects.filter(region__id=region_pk)
        data = [{'district_name': district.name,
                 'district_value': district.value} for district in districts_list]
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponseBadRequest()


def parse(request):
    if request.method == 'POST':
        form = ParseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_array = Parse.objects.order_by('-id')[:1]
            file_object = file_array[0]
            to_db(file_object.file_name)
            return redirect('success')
    else:
        form = ParseForm()

    return render(request, 'regions_data/parse.html', locals())


def success(request):
    return render(request, 'regions_data/success.html', locals())


def to_db(file):
    file = 'uploads/{}'.format(file)
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        region = ''
        for row in reader:
            if row[0] == region:
                new_district = District()
                new_district.region = region_object
                new_district.name = row[1]
                new_district.value = row[2]
                new_district.save()
            else:
                region_query = Region.objects.filter(name=row[0])
                if len(region_query) > 0:
                    region_object = region_query[0]
                    new_district = District()
                    new_district.region = region_object
                    new_district.name = row[1]
                    new_district.value = row[2]
                    new_district.save()
                    region = region_object.name
                else:
                    region_object = Region()
                    region_object.name = row[0]
                    region_object.save()

                    new_district = District()
                    new_district.region = region_object
                    new_district.name = row[1]
                    new_district.value = row[2]
                    new_district.save()
                    region = region_object.name
