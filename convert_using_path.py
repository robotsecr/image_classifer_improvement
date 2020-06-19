import os
from convertToJPG import main2
#data_dir='images_y/class2'
obj0=main2()
def convertAllImages(data_dir):
	#get path of every image
	try:
		for img in os.listdir(data_dir):
			fullpath=data_dir+"/"+img
			print(fullpath)
			# convert image using path
			obj0.convertImageUsingPath(fullpath)
	except Exception as e :
		print (e)
		
def changeDirectorys(data_dir):
	path_for_orginal=data_dir.split("/")
	path_for_orginal=path_for_orginal[:len(path_for_orginal)-1]
	path_for_orginal='/'.join(path_for_orginal)
	print(path_for_orginal)
	try:
		os.replace(data_dir,data_dir+"_orginal")
		os.mkdir(data_dir)
		return 1
	except Exception as e:
		print("file same Exists : ",e)
		return 0
	
	
	
	#print(path_for_orginal)
#changeDirectorys("images_y/class2")
	
