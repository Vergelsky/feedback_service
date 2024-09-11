from rest_framework.generics import CreateAPIView, RetrieveAPIView

from tg_questions.models import Survey
from tg_questions.serializers import SurveySerializer, ResponseSerializer

from django.http import Http404


class ResponseCreateView(CreateAPIView):
    serializer_class = ResponseSerializer


class SurveyRetrieveView(RetrieveAPIView):
    serializer_class = SurveySerializer

    def get_object(self):
        survey = Survey.objects.filter(is_active=True).order_by('-created_at').first()
        if not survey:
            raise Http404("Книга не найдена")
        return survey
