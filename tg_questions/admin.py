from django.contrib import admin

from tg_questions.models import Survey, Response, Question, Choice, UserResponse


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'is_permanent', 'expiration_date')
    list_display_links = ('title',)




@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'text', 'order')
    list_display_links = ('survey',)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')
    list_display_links = ('question',)

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('survey', 'client', 'completed_at')
    list_display_links = ('client',)


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('response', 'question', 'choice')
    list_display_links = ('response',)