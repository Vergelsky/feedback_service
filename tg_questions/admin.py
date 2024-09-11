from django.contrib import admin

from tg_questions.models import Survey, Response, Question, Choice, UserResponse


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'is_permanent', 'expiration_date')


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'client')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'order')


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'question', 'text', 'order')


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'response', 'question', 'choice')