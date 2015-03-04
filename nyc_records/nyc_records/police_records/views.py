import csv
import json

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response

# from .forms import UploadFileForm


class UploadRecord(LoggedInMixin, View):

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
        else:
            form = UploadFileForm()
        return render_to_response('upload_record.html', {'form': form})


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()