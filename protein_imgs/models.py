from django.db import models
from django.core import validators

class ProteinDataViz(models.Model):
    '''Django model for the data visualization

    '''
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, blank=True, default='')
    created_by_version = models.CharField(max_length=200, blank=False)
    created_by_version.validators = [validators.int_list_validator(sep='.')]
    viz_category = models.CharField(max_length=200, blank=True, default='')
    vis_file = models.FileField(upload_to='uploads/%Y/%m/%d')
