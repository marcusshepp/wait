from rest_framework import serializers
from .models import Workout, Exercise, Cardio, SetMeister

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class SetMeisterSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = SetMeister
        fields = '__all__'

class CardioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardio
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    set_meister = SetMeisterSerializer(many=True, read_only=True)
    cardio_sessions = CardioSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'date_created', 'notes', 'set_meister', 'cardio_sessions']
        read_only_fields = ['id', 'date_created', 'set_meister', 'cardio_sessions']

class WorkoutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'notes']
        read_only_fields = ['id']
