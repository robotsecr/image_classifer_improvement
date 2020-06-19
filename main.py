
#### changes in main_for_training.py for classifyed  images and the path ###
from convert_using_path import convertAllImages,changeDirectorys
from main_for_training import main_for_t
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p','--pathofimagetoconvert', help='...The source image path',required=False)
parser.add_argument('-s','--sourceimage', help='...The source image',required=True)
args = parser.parse_args()
# if there file for png images convert it 
if args.pathofimagetoconvert:
	key=changeDirectorys(args.pathofimagetoconvert)
	# see if the new file exsist or create one 
	if key==0:
		pass
	else:
		convertAllImages(args.pathofimagetoconvert)	
	main_for_t
#else train easy
else:
	#callthetraining()
	main_for_t(args.sourceimage)
	
	
	
