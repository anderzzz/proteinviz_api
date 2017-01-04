from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render
#from django.forms import ModelFormWithFileField
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from protein_imgs.models import ProteinDataViz
from protein_imgs.serializers import ProteinDataVizSerializer

class JSONResponse(HttpResponse):
    '''An HttpResponse that renders its content into JSON.

    '''
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def proteindataviz_list(request):
    '''List all visualizations

    '''
    if request.method == 'GET':
        viz = ProteinDataViz.objects.all()
        serializer = ProteinDataVizSerializer(viz, many=True)
        return JSONResponse(serializer.data)

class ProteinDataVizList(ListView):
    model = ProteinDataViz

#def upload_file(request):
#    if request.method == 'POST':
#        form = ModelFormWithFileField(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/success/url')
#    else:
#        form = ModelFormWithFileField()
#    return render(request, 'upload.html', {'form': form})

