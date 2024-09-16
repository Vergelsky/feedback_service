from django import forms

from .models import Survey, Question, Choice


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


QuestionFormSet = forms.inlineformset_factory(Survey, Question, form=QuestionForm, extra=20, can_delete=True)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'


ChoiceFormSet = forms.inlineformset_factory(Question, Choice, form=ChoiceForm, extra=10, can_delete=True)
