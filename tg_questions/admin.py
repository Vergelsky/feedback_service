from django.contrib import admin

from tg_questions.models import Survey, Response, Question, Choice, UserResponse


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'is_permanent', 'expiration_date')
    list_display_links = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'survey', 'order')
    list_display_links = ('text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question__survey', 'question', 'is_right_answer')
    list_display_links = ('text',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('client', 'survey', 'completed_at', 'is_success')
    list_display_links = ('client',)


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    def get_choice_is_right_answer(self, obj):
        return obj.choice.is_right_answer

    get_choice_is_right_answer.short_description = 'Правильный ответ'
    get_choice_is_right_answer.boolean = True

    list_display = ('response', 'question', 'choice', 'get_choice_is_right_answer')
    list_display_links = ('response',)



