from django.core.management.base import BaseCommand
from django.utils import timezone
from tg_questions.models import Survey


class Command(BaseCommand):
    help = 'Deactivate expired surveys'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_surveys = Survey.objects.filter(expiration_date__lt=now, is_active=True)
        count = expired_surveys.count()
        expired_surveys.update(is_active=False)
        self.stdout.write(self.style.SUCCESS(f'{count} опросов с истёкшим скроком отмечено неактивными.'))
