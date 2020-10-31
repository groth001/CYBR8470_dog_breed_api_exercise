class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']
