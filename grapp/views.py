from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation,Rental

# Create your views here.

def index(request):
    return HttpResponse('Welcome to the Test Task - Python Django Engineer/Remote GR 122 - by Dawood :)')

def reservations(request):
    """
    Fetches all reservations for given rentals from the database since we have no limit specified.
    In the real word, we assume that a given rental (room maybe?) can have only one reservation at any given time,
    so reservations must not overlap. Also, it is always valid that if the above condition is true and a rental has 1 or more
    reservations, then the first reservation entry has a previous reservation, i.e the first reservation has a preceding reservation.
    Otherwise, there is no preceding reservation for that given rental
    """
    rentals = Rental.objects.all()
    reservs = Reservation.objects.select_related().order_by('checkin')
    reservations_info = {}
    for rental in rentals:
        reservations_info['rental_'+str(rental.id)] = {
            'name': rental.name,
            'reservations': reservs.filter(rental=rental.id),
            'first_reserv_id': '-'
        }

    #Best way below is to use the templating system!
    info = '<!DOCTYPE html><html lang="en-US"> <head> <meta charset="utf-8"/> <title>Guest Ready Reservations</title> </head> <body><div><h2>Current Reservations</h2> <table style="border-collapse: collapse;"> <thead> <tr> <th style="border:1px solid #000000;padding:8px;">Rental Name</th> <th style="border:1px solid #000000;padding:8px;">ID</th> <th style="border:1px solid #000000;padding:8px;">Checkin</th> <th style="border:1px solid #000000;padding:8px;">Checkout</th> <th style="border:1px solid #000000;padding:8px;">Previous Reservation ID</th> </tr></thead><tbody>'
    for key in reservations_info:
        firstRow = True
        i = 0
        for reservation in reservations_info[key]['reservations']:
            info += '<tr>'
            info += '<td style="border:1px solid #000000;padding:8px;">'+str(reservation.rental)+'</td>'
            info += '<td style="border:1px solid #000000;padding:8px;">'+str(reservation.id)+'</td>'
            info += '<td style="border:1px solid #000000;padding:8px;">'+str(reservation.checkin)+'</td>'
            info += '<td style="border:1px solid #000000;padding:8px;">'+str(reservation.checkout)+'</td>'
            if firstRow:
                info += '<td style="border:1px solid #000000;padding:8px;">'+reservations_info[key]['first_reserv_id']+'</td>'
                firstRow = False
            else:
                info += '<td style="border:1px solid #000000;padding:8px;">'+str(reservations_info[key]['reservations'][i].id)+'</td>'
                i += 1
            info += '</tr>'
    info += '</tbody></body></html>'

    return HttpResponse(info)