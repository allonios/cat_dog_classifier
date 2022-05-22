import numpy as np
from keras.applications.mobilenet_v2 import decode_predictions
from keras.applications.mobilenet_v2 import preprocess_input
from django.conf import settings

def predict(image):
    np_image = np.array(image.resize((224, 224)))
    data = preprocess_input(np.expand_dims(np_image, axis=0))
    predictions = settings.MODEL.predict(data)
    decoded_predictions = decode_predictions(predictions)[0]
    return decoded_predictions[0]
