#!/usr/bin/python3
import os
import cv2
import time
IMG_SIZE=500
def create_training_data(datadir):
			path=datadir
			#path=os.path.join(datadir,catg)
			#class_num=categories.index(catg)
			for img in os.listdir(path):
				try :
					 img_array = cv2.imread(os.path.join(path, img))
					 new_array = cv2.resize(img_array, (700, IMG_SIZE))
					 print(img_array)
					 cv2.imshow('that is person',new_array)
					 cv2.waitKey(0)
					 cv2.destroyAllWindows()
					 #
					 #training_data.append([new_array, class_num])
				except Exception as e:
					print(e)
create_training_data('../images_y/class0')
