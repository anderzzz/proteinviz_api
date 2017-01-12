from server.presenter_webapp.models import PresenterDataViz
from server.presenter_webapp.serializers import PresenterDataVizSerializer
from django.http import Http404
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PresenterDataVizList(APIView):
    '''List all protein data visualization, or create new one

    '''
    def get(self, request, format=None):
        '''GET method'''
        viz = PresenterDataViz.objects.all()
        serializer = PresenterDataVizSerializer(viz, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        '''POST method'''
        serializer = PresenterDataVizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PresenterDataVizDetail(APIView):
    '''Retrieve, update or delete visualization instance

    '''
    def get_object(self, pk):
        try:
            return PresenterDataViz.objects.get(pk=pk)
        except PresenterDataViz.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''GET method'''
        viz = self.get_object(pk)
        serializer = PresenterDataVizSerializer(viz)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        '''PUT method'''
        viz = self.get_object(pk)
        serializer = PresenterDataVizSerializer(viz)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        '''DELETE method'''
        viz = self.get_object(pk)
        viz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PresenterViz(APIView):
    '''Retrieve visualization file at given path

    '''
    def get_object(self, pk):
        try:
            return PresenterDataViz.objects.get(pk=pk)
        except PresenterDataViz.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''GET method'''
        viz = self.get_object(pk)
        serializer = PresenterDataVizSerializer(viz)
        file_dir = serializer.data['viz_file_path']
        with open(settings.BASE_DIR + file_dir) as fin:
            content = fin.read()
        template = loader.get_template('presenter_vizscroll/statement.html')
        context = {'content' : content}
        return Response(template.render(context, request))

class ViewViz(View):
    '''Simple view of HTML visualization

    '''
    def get_object(self, pk):
        try:
            return PresenterDataViz.objects.get(pk=pk)
        except PresenterDataViz.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''GET method'''
        viz = self.get_object(pk)
        serializer = PresenterDataVizSerializer(viz)
        file_dir = serializer.data['viz_file_path']
        with open(settings.BASE_DIR + file_dir) as fin:
            content = fin.read()
        template = loader.get_template('presenter_vizscroll/statement.html')
        context = {'content' : content}
        return HttpResponse(template.render(context, request)) 

from collections import namedtuple

AAA = namedtuple('AAA', ['title', 'created', 'created_by', 'div', 'script'])

class Dummy(View):
    '''Super simple stuff

    '''
    def get(self, request, format=None):
        '''GET method'''
        viz = PresenterDataViz.objects.all()
        coll = []
        for x in viz:
            created = x.created
            title = x.title
            created_by = x.created_by
            with open(x.viz_file_path + '_div') as fin:
                div = fin.read()
            with open(x.viz_file_path + '_script') as fin:
                script = fin.read()
            aaa = AAA(title, created, created_by, div, script)
            coll.append(aaa)
        template = loader.get_template('presenter_vizscroll/list_of_viz.html')
        context = {'posts' : coll}
        return HttpResponse(template.render(context, request)) 


