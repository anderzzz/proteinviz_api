from django.shortcuts import render
from django.views.generic import ListView
from protein_imgs.models import ProteinDataViz
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import ModelFormWithFileField

class ProteinDataVizList(ListView):
    model = ProteinDataViz

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})

