from django.shortcuts import render
from django.http import HttpResponse

from .forms import TestForm
from .models import FormSubmissions


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # use of ModelForm should allow this to save straight to DB
            form.save()
    else:
        form = FormSubmissions()

    return render(request, 'form.html', {'form': form})

def submissions(request):
    allSubmissions = FormSubmissions.objects.all()
    return render(request, 'submissions.html', {'data':allSubmissions })