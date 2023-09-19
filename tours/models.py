from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_start_end_dates(start_date, end_date):
    if start_date >= end_date:
        raise ValidationError("End date must be after start date")

class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        validate_start_end_dates(self.start_date, self.end_date)
        super(Tour, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tour = models.ForeignKey(Tour, related_name='destinations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    tour = models.ForeignKey(Tour, related_name='bookings', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.customer_name
