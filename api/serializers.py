from rest_framework import serializers
from api.models import Dog, Breed

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']
