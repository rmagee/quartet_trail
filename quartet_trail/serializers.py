from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    '''
    User Serializer for task history.
    '''
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class QuartetTrailSerializer(serializers.ModelSerializer):

    history_user = UserSerializer(read_only=True)
    
    class Meta:
        model = None
        fields = '__all__'

class QuartetTrailDeltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuartetTrailDelta
        fields = '__all__'
