#from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api.utils import get_lnglat, send_sms


@csrf_exempt
def ussd(request):
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
