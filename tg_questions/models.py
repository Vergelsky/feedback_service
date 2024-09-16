from django.db import models

from django.contrib.auth.models import User


class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель опроса")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=False, verbose_name="Активен")
    is_permanent = models.BooleanField(default=False, verbose_name="Постоянный")
    expiration_date = models.DateTimeField(blank=True, null=True, verbose_name="Срок действия")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE, verbose_name='К опросу')
    text = models.CharField(max_length=255, verbose_name='Текст')
    order = models.PositiveIntegerField(verbose_name='Номер')

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, verbose_name='Вариант ответа')
    text = models.CharField(max_length=255, verbose_name='Текст')
    order = models.PositiveIntegerField(default=1, verbose_name='Номер')

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"

    def __str__(self):
        return self.text


class Response(models.Model):
    client = models.CharField(max_length=255, default="Anonymous", verbose_name='Клиент')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name='Время окончания')

    class Meta:
        verbose_name = "Пройденный опрос"
        verbose_name_plural = "Пройденные опросы"

    def __str__(self):
        return f"Response by {self.client} for {self.survey}"


class UserResponse(models.Model):
    response = models.ForeignKey(Response, related_name='responses', on_delete=models.CASCADE, verbose_name='Пройденный опрос')
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE, verbose_name='Вопрос')
    choice = models.ForeignKey(Choice,  related_name='responses', on_delete=models.CASCADE, verbose_name='Выбранный ответ')

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователя"

    def __str__(self):
        return f"{self.question}: {self.choice}"
