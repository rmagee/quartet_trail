from os import path
from django.apps import apps
from rest_framework import viewsets
from . import serializers


class QuartetTrailViewSet(viewsets.ModelViewSet):

    @property
    def model(self):
        current_path = path.split(self.request.path)
        print(current_path[0])
        if current_path[0] == '/quartet-trail':
            tracked_model = current_path[1]
            historical_model = 'Historical' + tracked_model
            return apps.get_model('quartet_trail', model_name=historical_model)
        else:
            # Django Rest Framework requires a default when it loads.
            return apps.get_model('quartet_trail', model_name="HistoricalEndpoint")
        
    def get_queryset(self):
        model = self.model
        return model.objects.all()           

    def get_serializer_class(self):
        serializers.QuartetTrailSerializer.Meta.model = self.model
        return serializers.QuartetTrailSerializer
