# Model Training Code Sir ....
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)

x_train = train_datagen.flow_from_directory(r"../datset/train",target_size = (64,64),batch_size = 32)
x_test = test_datagen.flow_from_directory(r"../dataset/test",target_size = (64,64),batch_size = 32)

x_train.class_indices

model = Sequential()

model.add(Convolution2D(32,(3,3),input_shape = (64,64,3),activation = "relu"))

model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())

model.add(Dense(units = 128 , init = "uniform",activation = "relu"))

model.add(Dense(units = 2 , init = "uniform",activation = "softmax"))

model.compile(loss = "categorical_crossentropy",optimizer = "adam",metrics = ["accuracy"])

model.fit_generator(x_train, steps_per_epoch = 47,validation_data = x_test,validation_steps = 20 ,epochs = 10)

model.save("lungs.h5")
