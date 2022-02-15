from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TestForm
from .models import FormSubmissions


def index(request):
    form = TestForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # use of ModelForm should allow this to save straight to DB
            form.save()

    return render(request, 'form.html', {'form': form})

def submissions(request):
    allSubmissions = FormSubmissions.objects.all()
    return render(request, 'submissions.html', {'data':allSubmissions })

def delete(request):
    # not sure why the parameter is only available on GET
    id=request.GET.get('id', '')
    if(id != ''):
        FormSubmissions.objects.filter(id=id).delete()

    return HttpResponseRedirect('submissions')