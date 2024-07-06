from django.db import models
from PIL import Image
from keras.preprocessing.image import img_to_array
import cv2
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from django.conf import settings

class Digit(models.Model):
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=2, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the image first

        try:
            # Open the saved image
            img = Image.open(self.image.path)
            img_array = img_to_array(img)
            gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            resized_img = cv2.resize(gray_img, (28, 28), interpolation=cv2.INTER_AREA)

            # Normalize the image
            ready_img = resized_img.astype('float32') / 255
            ready_img = np.expand_dims(ready_img, axis=-1)
            ready_img = np.expand_dims(ready_img, axis=0)

            print("Image processed successfully")

            # Load the model once, cache it in a class variable
            if not hasattr(self, 'model'):
                model_path = os.path.join(settings.BASE_DIR, 'CNN_model.h5')
                self.model = load_model(model_path)
                print("Model loaded successfully")

            # Predict the digit
            pred = np.argmax(self.model.predict(ready_img))
            self.result = str(pred)
            print(f'classified as {pred}')
        except Exception as e:
            print(f'failed to classify: {e}')
            self.result = 'error'

        # Save the result
        super().save(update_fields=['result'])