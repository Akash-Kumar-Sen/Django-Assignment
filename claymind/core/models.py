from django.db import models
from core.common_utills.model_utills import UUIDTimeStampedModel


class ContactChoices(models.TextChoices):
    CHECKED = "Checked"
    NOT_CHECKED = "Not Checked"


class PersonData(UUIDTimeStampedModel):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    contact = models.CharField(max_length=50, choices=ContactChoices.choices, default=ContactChoices.NOT_CHECKED)
    order_value = models.IntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return str(self.email)