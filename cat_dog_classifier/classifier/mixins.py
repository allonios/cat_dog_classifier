import decimal

from PIL import Image

from classifier.utils import predict


class CatDogImageFormPredictionMixin:
    def predict(self, form):
        # this will write the image to our server.
        object = form.save(commit=True)
        # we will need to predict stuff here.
        prediction = predict(Image.open(object.image.path))
        class_ = prediction[1]
        confidence = prediction[2]

        object.label = class_
        object.confidence = decimal.Decimal(float(confidence))

        object.save()

        return {
            "class": class_,
            "confidence": object.confidence
        }