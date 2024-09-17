from rest_framework import serializers
from .models import Survey, Response, Question, Choice, UserResponse


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = '__all__'


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['question', 'choice']


class ResponseSerializer(serializers.ModelSerializer):
    responses = UserResponseSerializer(many=True)

    class Meta:
        model = Response
        fields = ['id', 'survey', 'client', 'completed_at', 'responses']

    def create(self, validated_data):
        print(validated_data)
        user_responses_data = validated_data.pop('responses')
        response = Response.objects.create(**validated_data)
        for user_response_data in user_responses_data:
            UserResponse.objects.create(response=response, **user_response_data)
        return response
