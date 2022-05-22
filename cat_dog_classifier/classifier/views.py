from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView

from classifier.forms import CatDogLogsForm
from classifier.mixins import CatDogImageFormPredictionMixin
from classifier.models import CatDogLogs


class ClassifierImageUploadView(FormView, CatDogImageFormPredictionMixin):
    template_name = "upload_page.html"
    form_class = CatDogLogsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logs"] = CatDogLogs.objects.all()
        return context

    def form_valid(self, form):
        return render(
            request=self.request,
            template_name="display_class.html",
            context=self.predict(form),
        )


class ClassifierImageUploadAPIView(FormView, CatDogImageFormPredictionMixin):
    template_name = "upload_page.html"
    form_class = CatDogLogsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logs"] = CatDogLogs.objects.all()
        return context

    def form_valid(self, form):
        return JsonResponse(self.predict(form))
