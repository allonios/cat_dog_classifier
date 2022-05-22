from django.db import models
from django.utils.translation import gettext_lazy as _


class CatDogLogs(models.Model):
    CAT = "cat"
    DOG = "dog"

    CLASSES = (
        (CAT, _("It's a Citty.")),
        (DOG, _("It's a Doggo."))
    )

    image = models.ImageField(verbose_name=_("Image"), upload_to="media/",)
    label = models.CharField(
        verbose_name=_("Image Class/Label"), choices=CLASSES, max_length=30,
    )
    confidence = models.DecimalField(
        verbose_name=_("Prediction Confidence"),
        max_digits=5,
        decimal_places=2,
        null=True
    )
