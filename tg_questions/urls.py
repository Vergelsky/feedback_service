from django.urls import path

from tg_questions.views import ResponseCreateView, SurveyRetrieveView, SurveyCreateAPIView, SurveyFormView

urlpatterns = [
    path('form/', SurveyFormView.as_view(), name='update_survey'),
    path('api/create-survey/', SurveyCreateAPIView.as_view(), name='create_survey'),
    path('api/get-survey/', SurveyRetrieveView.as_view(), name='get_survey'),
    path('api/load-response/', ResponseCreateView.as_view(), name='load_response'),
]

