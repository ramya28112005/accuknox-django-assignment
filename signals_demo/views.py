from django.http import HttpResponse
from django.db import transaction

from .models import TestModel


def test_signal_view(request):

    try:

        with transaction.atomic():

            TestModel.objects.create(
                name="Ramya"
            )

            raise Exception(
                "Force rollback"
            )

    except Exception:
        pass

    return HttpResponse(
        "Transaction Test Completed"
    )