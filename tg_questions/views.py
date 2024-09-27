from rest_framework.generics import CreateAPIView, RetrieveAPIView

from django.views.generic import CreateView, UpdateView

from tg_questions.form import SurveyForm, QuestionForm, QuestionFormSet, ChoiceFormSet
from tg_questions.models import Survey, Question, Choice
from tg_questions.create_serializers import CreateSurveySerializer
from tg_questions.serializers import SurveySerializer, ResponseSerializer

from django.http import Http404


class ResponseCreateView(CreateAPIView):
    serializer_class = ResponseSerializer


class SurveyRetrieveView(RetrieveAPIView):
    serializer_class = SurveySerializer

    def get_object(self):
        survey = Survey.objects.filter(is_active=True).order_by('-created_at').first()
        if not survey:
            raise Http404("Опрос не найден")
        return survey


class SurveyCreateAPIView(CreateAPIView):
    serializer_class = CreateSurveySerializer # В отдельном файле!
    queryset = Survey.objects.all()


class SurveyFormView(CreateView):
    model = Survey
    template_name = 'tg_questions/form.html'
    form_class = SurveyForm

# попытка сделать через формсеты (не работает)
#
#
# class SurveyCreateView(CreateView):
#     model = Survey
#     template_name = 'tg_questions/survey_form.html'
#     form_class = SurveyForm
#
#     def get_success_url(self):
#         return reverse_lazy('update_survey', kwargs={'pk': self.object.pk})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.method == 'POST':
#             question_formset = QuestionFormSet(self.request.POST, instance=self.object)
#         else:
#             question_formset = QuestionFormSet(instance=self.object)
#         context['question_form'] = question_formset
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         question_formset = context['question_formset']
#
#         if question_formset.is_valid():
#             response = super().form_valid(form)
#             question_formset.instance = self.object
#             question_formset.save()
#             return response
#         return self.form_invalid(form)
#
#
# class SurveyUpdateView(UpdateView):
#     model = Survey
#     template_name = 'tg_questions/survey_form.html'
#     form_class = SurveyForm
#
#     def get_success_url(self):
#         return reverse_lazy('update_survey', kwargs={'pk': self.object.pk})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         if self.request.method == 'POST':
#             question_formset = QuestionFormSet(self.request.POST, instance=self.object)
#         else:
#             question_formset = QuestionFormSet(instance=self.object)
#
#         context['question_formset'] = question_formset
#         return context
#
#     def form_valid(self, form):
#         question_formset = self.get_context_data()['formset']
#
#         if question_formset.is_valid():
#             response = super().form_valid(form)
#             question_formset.instance = self.object
#             question_formset.save()
#             return response
#
#         return super().form_invalid(form)
