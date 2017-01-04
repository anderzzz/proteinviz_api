'''Model definitions, which corresponds to how the data is structured and
defined, as it is exposed to the API.

'''
from django.db import models
from django.core import validators

class ProteinDataViz(models.Model):
    '''Django model for the data visualization

    '''
    WHO_ENTERED = (
        ('H1', 'Human One'),
        ('H2', 'Human Second'),
        ('S1', 'Software One'))

    title = models.CharField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, blank=True, default='',
                                  choices=WHO_ENTERED)
    created_by_version = models.CharField(max_length=200, blank=False)
    created_by_version.validators = [validators.int_list_validator(sep='.')]
    viz_category = models.CharField(max_length=200, blank=False, default='')
    viz_file_path = models.CharField(max_length=500, blank=False, default='')

    class Meta:
        '''Meta class to define attribute to order'''
        ordering = ('created',)
