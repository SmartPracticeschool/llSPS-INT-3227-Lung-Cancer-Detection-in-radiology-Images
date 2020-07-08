# flask code sir !!
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow as tf
from flask import Flask, request , render_template

graph = tf.get_default_graph()
model = load_model("lungs.h5")
index = ["Affected","Normal"]

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
   
    if request.method == 'POST':
        global model
        global index
        global graph
        f = request.files['image']
        img = Image.open(f)
        img = img.resize((64,64))
        img = img.convert(mode='RGB')
        x = image.img_to_array(img)

        x = np.expand_dims(x,axis = 0)
        x.shape
        with graph.as_default():
            predicted = model.predict_classes(x)
            return index[predicted[0]]

if __name__ == '__main__': 
    app.run() 