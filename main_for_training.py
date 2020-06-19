from matplotlib.image import imread
import matplotlib.pyplot as plt
import codecs,json
import tensorflow as tf
import numpy as np
from tensorflow import keras
import random
import os
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from convertToJPG  import main2
training_data=[]
test_dat=[]
IMG_SIZE=50
img_size=50
#++++++++++++++++++++++++++++++++++
catag_i=["real person","cartoon/anime","lightpicture/somethingelse"] #change
categories=["class0","class1","class2"]#change
file_list=[]
class_list=[]
#+++++++++++++++++++++++++++++++++++++++++++++++++
datadir="images_y" #change
class PrepereDirectoys():
	def create_training_data(self):
		for catg in categories:
			path=os.path.join(datadir,catg)
			class_num=categories.index(catg)
			for img in os.listdir(path):
				try :
					 img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
					 new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
					 training_data.append([new_array, class_num])
				except Exception as e:
					 pass
	def Read_Img_From_User(self,x):
		user_img=[]
		try:
			img=cv2.imread(x,cv2.IMREAD_GRAYSCALE)
			img0=cv2.resize(img,(IMG_SIZE,IMG_SIZE))
			user_img.append(img0)
			return user_img
		except Exception as e:
			print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("There is problem with your path image check again  : ",e)
			print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			exit()
	def showImage(self,img,cate):
		img_array = cv2.imread(img)
		new_array = cv2.resize(img_array, (700, 500))
		cv2.imshow(cate,new_array)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

def main_for_t(sourceimage):
	obj0=PrepereDirectoys()
	obj1=main2()
	obj0.create_training_data()
	user_img=[]
	#testt_data()
	#x0=obj1.arguments()
	#x=x0.sourceimage
	user_img=obj0.Read_Img_From_User(sourceimage)
	print("test_data size,",test_dat)
	user_img=np.array(user_img).reshape(-1,IMG_SIZE,IMG_SIZE,1)
	user_img=user_img/255.0
	random.shuffle(training_data)
	X=[]
	y=[]
	counter=0
	for features, label in training_data:
		#print('features:',features)
		#print('labels:',label)

		X.append(features)
		y.append(label)

	X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
	y=np.array(y)
	X=X/255.0
	x_t=[]
	y_t=[]
	if test_dat!=[]:
		for features, label in test_dat:
			counter=counter+1
			x_t.append(features)
			y_t.append(label)

	x_t=np.array(x_t).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
	y_t=np.array(y_t)
	x_t=x_t/255.0
	try:
		model=load_model("my_model.h5")
	except:
		model = Sequential()
		# 3 convolutional layers
		model.add(Conv2D(32, (3, 3), input_shape = X.shape[1:]))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2,2)))

		model.add(Conv2D(64, (3, 3)))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2,2)))

		model.add(Conv2D(64, (3, 3)))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2,2)))
		model.add(Dropout(0.25))

		# 2 hidden layers
		model.add(Flatten())
		model.add(Dense(128))
		model.add(Activation("relu"))

		model.add(Dense(128))
		model.add(Activation("relu"))

		# The output layer with 13 neurons, for 13 classes
		model.add(Dense(13))
		model.add(Activation("softmax"))

		# Compiling the model using some basic parameters
		model.compile(loss="sparse_categorical_crossentropy",
						optimizer="adam",
						metrics=["accuracy"])

		# Training the model, with 40 iterations
		# validation_split corresponds to the percentage of images used for the validation phase compared to all the images
		history = model.fit(X, y, batch_size=32, epochs=40, validation_split=0.1)
		#save model
		model.save("my_model.h5")
	if user_img.size>0:
		output=model.predict_classes([user_img])
		os.system('clear')#change of windows
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("the answer:",catag_i[output[0]])
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		obj0.showImage(sourceimage,catag_i[output[0]])
	else:
		print("wrong")
		
