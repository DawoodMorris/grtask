from django.test import TestCase
from .models import Rental, Reservation
import datetime
from django.utils import timezone

# Create your tests here.

class ReservationModelTest(TestCase):
    """
    Test cases for the Reservation model
    """

    def test_reject_past_checkin_date(self):
        """
        We cannot save a checkin of a past date
        """
        rental = Rental(name='Rental 3')
        rental.save()
        rsv = Reservation()
        rsv.checkin = timezone.now() + datetime.timedelta(days=-2) #a past date from yestarday backwards
        rsv.checkout = timezone.now() + datetime.timedelta(days=10)
        rsv.rental = rental
        self.assertFalse(rsv.save(),False)
    
    def test_reject_past_checkout_date(self):
        """
        We cannot save a checkout of a past date
        """
        rental = Rental(name='Rental 1')
        rental.save()
        rsv = Reservation()
        rsv.checkin = timezone.now() + datetime.timedelta(days=+2)
        rsv.checkout = timezone.now() + datetime.timedelta(days=-10) #a past date from yestarday backwards
        rsv.rental = rental
        self.assertFalse(rsv.save(),False)

class RentalModelTest(TestCase):
    """
    Test cases for the Rental model
    """
    def test_reject_invalid_rental_name(self):
        """
        We cannot save a Rental with an invalid rental name
        """
        rental = Rental(name='')
        self.assertFalse(rental.save(),False)

    def test_reject_a_too_long_rental_name(self):
        """
        We cannot save a Rental with a very long (longer than sensible name) rental name
        """
        rental = Rental(name='This is a very long name which cannot be in the real world of business')
        self.assertFalse(rental.save(),False)
