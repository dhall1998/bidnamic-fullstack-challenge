from django import forms
from django.core.exceptions import ValidationError

from datetime import date,datetime, timedelta
import re

from .models import FormSubmissions

BIDDING_SETTINGS = [ ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')]
TITLES = [ ('', ''),('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr')]

def validate_dateOfBirth(providedDate):
    currentDate = date.today()

     # work out 18 years prior to today
    latestAllowedDate = date(currentDate.year - 18, currentDate.month, currentDate.day)

    if providedDate <= latestAllowedDate:
        return providedDate
    else:
        raise ValidationError('You must be over 18 years old to submit this form')

def validate_phoneNumber(providedPhoneNumber):
    # remove whitespace and non-numeric characters from phonenumber for validation
    formattedPhoneNumber = re.sub('\D|\_|\-', '', providedPhoneNumber)

    # match both +44 and 0 prefixed phone numbers
    if re.match('^((44)|(0))\d{10}$', formattedPhoneNumber):
        return formattedPhoneNumber
    else:
        raise ValidationError('Telephone Number must be a valid UK phone number, matching regex ^((44)|(0))\d{10}$')

def validate_googleAdsID(googleAdsID):
    if re.match('^\d{3}\-\d{3}\-\d{4}$', googleAdsID):
        return googleAdsID
    else:
        raise ValidationError('Google Ads Account ID must be in format XXX-XXX-XXXX')


class TestForm(forms.ModelForm):
    class Meta:
        model = FormSubmissions
        fields = [ 'title', 'firstName', 'lastName', 'dateOfBirth', 'companyName', 'address', 'telephoneNumber', 'biddingSettings', 'googleAdsID']

    title = forms.ChoiceField(label='Title',choices=TITLES, required=False)
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Surname', max_length=100)
    dateOfBirth = forms.DateField(label='Date Of Birth (YYYY-MM-DD)', validators=[validate_dateOfBirth])
    companyName = forms.CharField(label='Company Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100, widget=forms.Textarea(attrs={'rows':4, 'cols':15})) # Multiple lines?
    telephoneNumber = forms.CharField(label='Telephone Number', max_length=20, validators=[validate_phoneNumber]) # add validation to this?
    biddingSettings = forms.ChoiceField(label='Bidding Settings',choices=BIDDING_SETTINGS)
    googleAdsID = forms.CharField(label='Google Ads Account ID', max_length=12, validators=[validate_googleAdsID])
