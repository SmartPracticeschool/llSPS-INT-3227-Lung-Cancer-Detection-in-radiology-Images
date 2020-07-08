from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image

model = load_model("lungs.h5")
img = image.load_img(r"image_search_1593841591274.jpg",target_size = (64,64))

x = image.img_to_array(img)
x = np.expand_dims(x,axis = 0)
x.shape

ypred = model.predict_classes(x)

ypred

index = ["Affected","Normal"]
print(index[ypred[0]])
