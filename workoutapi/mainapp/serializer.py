from rest_framework import serializers
from .models import User, Exercises

""" User serializer """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'weight', 'age', 'height']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # This is hashing password
        instance.save()
        return instance


""" Exercise serializer """


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = ['name', 'description', 'instruction',
                  'target_muscles', 'exercise_type',
                  'rest_between_sets']
