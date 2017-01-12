from rest_framework import serializers
from protein_imgs.models import PresenterDataViz

#class ProteinDataVizSerializer(serializers.Serializer):
#    '''Serializer to translate between data in database and the format sent
#    over the HTTP request.
#
#    '''
#    id = serializers.IntegerField(read_only=True)
#    title = serializers.CharField(required=False, allow_blank=True,
#                                 max_length=200)
#    created = serializers.DateTimeField()
#    created_by = serializers.CharField(required=False, allow_blank=True,
#                                       max_length=200)
#    created_by_version = serializers.CharField(required=False,
#                                               allow_blank=True, max_length=200)
#    viz_category = serializers.CharField(max_length=200, allow_blank)
#
#    def create(self, validated_data):
#        '''Create and return an instance of `ProteinDataViz`, given the validated
#        data.
#
#        '''
#        return ProteinDataViz.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        '''Update and return an existing `ProteinDataViz` instance, given the
#        validated data.
#
#        '''
#        instance.viz_category = validated_data.get('viz_category', instance.viz_category)
#        instance.created = validated_data.get('created', instance.created)
#        instance.created_by = validated_data.get('crated_by', instance.created_by)
#        instance.title = validated_data.get('title', instance.title)
#        instance.created_by_version = validated_data.get('created_by_version',
#                                      instance.created_by_version)
#        instance.save()
#
#        return instance

class ProteinDataVizSerializer(serializers.ModelSerializer):
    '''Serializer to translate between data in database and the format sent
    over the HTTP request

    '''
    class Meta:
        model = PresenterDataViz
        fields = ('id', 'title', 'created', 'created_by', 'created_by_version',
                  'viz_category', 'viz_file_path')

