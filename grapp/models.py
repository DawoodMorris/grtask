from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Rental(models.Model):
    """
    A Rental Model. It has the following props/fields:
    name: The name of the rental
    """
    name = models.CharField(max_length=100)

    def save(self) -> bool:
        """
        Save rental information
        """
        if len(self.name) < 1:
            return False
        max_useful_name_length = 25
        if len(self.name) > max_useful_name_length:
            return False
        super().save()
        return True

    def __str__(self) -> str:
        """
        Return the string representaion (human readable format) of the rental name
        """
        return self.name




class Reservation(models.Model):
    """
    Reservation Model. It composes and manages reservations for Rentals. It has the following props/fields:
    rental_id: An integer also a foreign key which relates a given Reservation to a Rental.
    checkin: A date marking a checkin event
    checkout: A date marking a checkout event
    """
    rental = models.ForeignKey(Rental,on_delete=models.CASCADE)
    checkin = models.DateField('check in data') #This should be a datetime field! e.g YYY-MM-DD HH:MM:SS, but the task instructions specified YYY-MM-DD
    checkout = models.DateField('check out date')

    def save(self):
        """
        Save the reservation information
        """
        if self.checkin < timezone.now():
            return False
        if self.checkout < timezone.now():
            return False
        super().save()
        return True