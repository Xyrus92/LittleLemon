from django.db import models

# Create your models here.
class Booking(models.Model):
    #id = models.SmallIntegerField(default=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=6)
    booking_date = models.DateTimeField()


# Add code to create Menu model
class Menu(models.Model):
    #id = models.SmallIntegerField(default=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=5)