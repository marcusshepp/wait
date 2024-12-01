from rest_framework import serializers
from .models import Workout, Exercise, Sett, Cardio

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class SetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = Sett
        fields = '__all__'

class CardioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardio
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True, read_only=True)
    cardio_sessions = CardioSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'date_created', 'notes', 'sets', 'cardio_sessions']
        read_only_fields = ['id', 'date_created', 'sets', 'cardio_sessions']

class WorkoutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'notes']
        read_only_fields = ['id']
