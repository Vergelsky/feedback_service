from django.urls import path

from tg_questions.views import ResponseCreateView, SurveyRetrieveView

urlpatterns = [
    path('api/get-survey/', SurveyRetrieveView.as_view(), name='get_survey'),
    path('api/load-response/', ResponseCreateView.as_view(), name='load_response'),
]
