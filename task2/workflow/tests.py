from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.timezone import now

from workflow.models import Procedure, ProcedureExecution


class TestProcedureExecution(TestCase):
    def test_model(self):
        """
        Тест уникальности выполняемых процедур
        """
        procedure1 = Procedure.objects.create(name='first')
        procedure2 = Procedure.objects.create(name='second')

        user1 = User.objects.create(username='first_user')

        ProcedureExecution.objects.create(procedure=procedure1, employee=user1)
        ProcedureExecution.objects.create(procedure=procedure2, employee=user1)

        action = ProcedureExecution(procedure=procedure1, employee=user1)
        with self.assertRaises(ValidationError):
            action.validate_unique()

        three_days_ago = now() - timedelta(days=3)
        action.date_create = three_days_ago
        action.validate_unique()
        action.save()
        self.assertTrue(action.id)
        # обход auto_now_add
        ProcedureExecution.objects.filter(procedure=action.id).update(datetime_create=three_days_ago)
