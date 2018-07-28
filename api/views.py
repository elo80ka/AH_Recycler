#from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api.utils import get_lnglat, send_sms
from subscriber.models import Subscriber, Dropoff


def users(request):
    phone = request.GET.get('number')
    score = Dropoff.objects.filter(subscriber__phone=phone).count() * 10
    return JsonResponse({'score': score})


@csrf_exempt
def dropoff(request):
    print(request.POST)
    txt = request.POST['text']
    # phone = request.POST['phoneNumber']
    parts = txt.split('*')
    if not txt:
        return HttpResponse('CON Please enter the phone number')
    elif len(parts) == 1:
        phone = parts[0]
        try:
            client = Subscriber.objects.get(phone=phone)
        except Subscriber.DoesNotExist:
            client = Subscriber.objects.create(phone=phone)
        return HttpResponse(
            'CON Please enter the data in format NUMBOTTLES,NUMBAGS')
    else:
        phone = parts[0]
        num_bottles = parts[1].split(',')[0]
        num_bags = parts[1].split(',')[1]
        client = Subscriber.objects.get(phone=phone)
        Dropoff.objects.create(
            subscriber=client,
            num_bottles=num_bottles,
            num_bags=num_bags)
        score = Dropoff.objects.filter(subscriber=client).count() * 10
        msg = 'Number of points for {} is {}'.format(phone, score)
        return HttpResponse('END Thank you. ' + msg)


@csrf_exempt
def centers(request):
    print(request.POST)
    txt = request.POST['text']
    phone = request.POST['phoneNumber']
    if not txt:
        return HttpResponse('CON Please enter your address')
    else:
        address = request.POST['text']
        locations = get_center_locations(address)
        msg = '\n'.join([loc['address'] for loc in locations])
        #msg = 'Testing again'
        send_sms(msg, phone)
        return HttpResponse('END Thank you, we will send the nearby collection centers by SMS')
    #return HttpResponse('END Thanks')
    #return JsonResponse({'status': 'ok'})


def get_points(request):
    return JsonResponse({'points': 50})


def get_center_locations(address):
    return [
        {
            'address': '10, Ademola St',
            'lng': 3.567,
            'lat': 6.567
        },
        {
            'address': '10, Ademola St',
            'lng': 3.567,
            'lat': 6.567
        },
        {
            'address': '10, Ademola St',
            'lng': 3.567,
            'lat': 6.567
         }
    ]


def get_locations(request):
    address = request.GET.get('address')
    lng_lat = get_lnglat(address)
    print(address)
    centers = get_center_locations(address)
    return JsonResponse(
        {
            'location': lng_lat,
            'centers': centers
        }
    )
