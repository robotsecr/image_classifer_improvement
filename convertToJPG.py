#!/usr/bin/python3 
### ++++++++++++++++++++++ =>  convert using arguments , or file path  <=+++++++++++++++++++####
from PIL import Image
import argparse 
import os
import re
class main2:
	''''def arguments(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-s','--sourceimage', help='...The source image',required=True)
		args = parser.parse_args()
		return args'''
	def convertAlgorithm(self,sourceimage,new_path):
		k=-1
		im2=sourceimage.split('.')
		n=re.search("[a-zA-z\d\-\_\ ]+\.",sourceimage)
		# become images_y/*.
		im3=new_path+"/"+n.group()
		# 1) check file existes 2) convert uusing pli to  .jpg
		# 3) check if input,./mdekd.png or mdekd.png
		#print("ok",im3)
		try:
			im1 = Image.open(sourceimage)
			k=sourceimage.index(".")
			if k==0:
				newImageString="."+im3+"jpg"
			else:
				newImageString=im3+"jpg"
		except Exception as e:
			print("No such file or directory",e)
			exit()
		try:
			print("here:" ,newImageString)
			im1.save(newImageString)
		except Exception as e:
			print("image format problem : ",e)
			exit()
		
		# save the file test if the image type is wrong like icons
		
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	''''def convertImageUsingArg(self):
		args=self.arguments()
		sourceimage=args.sourceimage
		# calling
		self.convertAlgorithm(sourceimage)'''
	def  convertImageUsingPath(self,x):
		#get the file change path ===> images_y/calss2
		new_path=""
		path=x
		path=path.split('/')
		second_part=re.search("class\d",x)
		new_path='/'.join(path[:len(new_path)-2])+"/"+second_part.group()
		self.convertAlgorithm(x,new_path)
		#print("here :  ",new_path)
		
	
if __name__=="__main__":
	obje=main2()
	obje.arguments()
	obje.convertImageUsingArg()
