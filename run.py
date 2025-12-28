from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing import image
import sys


model = keras.models.load_model('CATDOG-###.h5') # Change to the correct model version (for example: "CATDOG_1-2M.h5" or "CATDOG_315-2k.h5")


def predict_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    predictions = model.predict(img_array)
    cat_prob, dog_prob = predictions[0]

    dog_percentage = dog_prob * 100
    cat_percentage = cat_prob * 100

    print(f"Dog: {dog_percentage:.2f}%, Cat: {cat_percentage:.2f}%")
    
    if dog_percentage > cat_percentage:
        print("It's a DOG!")
    else:
        print("It's a CAT!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the file path to the image.")
    else:
        image_path = sys.argv[1]
        predict_image(image_path)