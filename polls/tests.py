import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_created_recently(self):
        past = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        q = Question('Hello World?', created_at=past)
        self.assertIs(q.was_created_recently(), True)