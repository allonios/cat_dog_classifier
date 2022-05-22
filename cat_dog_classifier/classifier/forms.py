from django.forms import ModelForm

from classifier.models import CatDogLogs

class CatDogLogsForm(ModelForm):
    class Meta:
        model = CatDogLogs
        fields = ("image", )
