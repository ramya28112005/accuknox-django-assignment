from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel, SignalLog

import time
import threading


@receiver(post_save, sender=TestModel)
def my_signal(sender, instance, created, **kwargs):

    print("Signal Started")

    print(
        "Thread inside signal:",
        threading.current_thread().ident
    )

    time.sleep(5)

    SignalLog.objects.create(
        message="Created by Signal"
    )

    print("Signal Finished")