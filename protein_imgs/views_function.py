from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from protein_imgs.models import ProteinDataViz
from protein_imgs.serializers import ProteinDataVizSerializer

@api_view(['GET', 'POST'])
def proteindataviz_list(request, format=None):
    '''List all visualizations

    '''
    if request.method == 'GET':
        viz = ProteinDataViz.objects.all()
        serializer = ProteinDataVizSerializer(viz, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProteinDataVizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proteindataviz_detail(request, pk, format=None):
    '''Retrieve, update or delete a visualization

    '''
    try:
        viz = ProteinDataViz.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProteinDataVizSerializer(viz)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProteinDataVizSerializer(viz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        viz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

