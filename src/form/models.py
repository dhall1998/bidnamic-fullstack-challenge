from django.db import models
from django.core.exceptions import ValidationError

from datetime import date,datetime, timedelta
import re

BIDDING_SETTINGS = [ ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')]
TITLES = [ ('', ''),('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr')]


class FormSubmissions(models.Model):
    title = models.CharField(choices=TITLES, max_length=4)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    companyName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephoneNumber = models.CharField(max_length=12)
    biddingSettings = models.CharField(choices=BIDDING_SETTINGS, max_length=6)
    googleAdsID = models.CharField(max_length=12)
