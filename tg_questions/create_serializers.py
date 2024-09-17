from rest_framework import serializers
from tg_questions.models import Survey, Question, Choice


class CreateChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['text']

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)


class CreateQuestionSerializer(serializers.ModelSerializer):
    choices = CreateChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'order', 'choices']

    def create(self, validated_data):
        choices = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        for choice in choices:
            choice['question'] = question
            CreateChoiceSerializer().create(choice)
        return question


class CreateSurveySerializer(serializers.ModelSerializer):
    questions = CreateQuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ['title', 'description', 'is_active', 'is_permanent', 'expiration_date', 'questions']
        read_only_fields = ['user']

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

    def create(self, validated_date):
        questions = validated_date.pop('questions', [])
        survey = Survey.objects.create(**validated_date)
        for question in questions:
            question['survey'] = survey
            CreateQuestionSerializer().create(question)
        return survey
