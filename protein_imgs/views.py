from protein_imgs.models import ProteinDataViz
from protein_imgs.serializers import ProteinDataVizSerializer
from django.http import Http404
from django.template import loader
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProteinDataVizList(APIView):
    '''List all protein data visualization, or create new one

    '''
    def get(self, request, format=None):
        '''GET method'''
        viz = ProteinDataViz.objects.all()
        serializer = ProteinDataVizSerializer(viz, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        '''POST method'''
        serializer = ProteinDataVizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProteinDataVizDetail(APIView):
    '''Retrieve, update or delete visualization instance

    '''
    def get_object(self, pk):
        try:
            return ProteinDataViz.objects.get(pk=pk)
        except ProteinDataViz.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''GET method'''
        viz = self.get_object(pk)
        serializer = ProteinDataVizSerializer(viz)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        '''PUT method'''
        viz = self.get_object(pk)
        serializer = ProteinDataVizSerializer(viz)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        '''DELETE method'''
        viz = self.get_object(pk)
        viz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProteinViz(APIView):
    '''Retrieve visualization file at given path

    '''
    def get_object(self, pk):
        try:
            return ProteinDataViz.objects.get(pk=pk)
        except ProteinDataViz.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''GET method'''
        viz = self.get_object(pk)
        serializer = ProteinDataVizSerializer(viz)
        file_dir = serializer.data['viz_file_path']
        with open(settings.BASE_DIR + file_dir) as fin:
            content = fin.read()
        template = loader.get_template('protein_imgs_web/statement.html')
        context = {'content' : content}
        return Response(template.render(context, request))
