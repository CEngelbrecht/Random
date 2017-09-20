# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
import re
import matplotlib.pyplot as plt

#Locations of data on still frames, in pixels: rectangle definded by two points (upper left x, upper left y, lower right x, lower right y)

total_coords = (1320,1040,1660,1060)

#Open frame from video 

images = ['ffmpeg_'+str(i)+'.bmp' for i in range(166,4206)]

total = 0.0
successes = 0.0

kero_data = []
helium_data = []
lox_data = []

def get_kero(total_text):
	'''Search through text and extract kero value'''

	match = re.findall(r"KERO : \d+[^\w]",total_text) #[^\w] makes sure no letters are included

	value = float(match[0].split()[2][:-1]) #takes list, splits into components, grabs value, chops off trailing comma, typecasts to float

	return value


def get_helium(total_text):

	match = re.findall(r"HELIUM : \d+[^\w]",total_text)

	value = float(match[0].split()[2][:-1])

	return value


def get_lox(total_text):
	
	#print total_text

	match = re.findall(r"LOX : \d+",total_text)


	if len(match) < 1: 
		match = re.findall(r"Lox : \d+",total_text)
	
	value = float(match[0].split()[2]) #No trailing comma here

	return value
for image in images: 

	img = Image.open(image)

	total_crop = img.crop((total_coords))

	total_text = pytesseract.image_to_string(total_crop)

	#print total_text

	if re.match(r"(.+)?KERO : \d+, HELIUM : \d+, (LOX|Lox) : \d+(?!\w)", total_text): #
		print(total_text,image)

		kero_data.append(get_kero(total_text))
		helium_data.append(get_helium(total_text))
		lox_data.append(get_lox(total_text))

		

		successes += 1

	total+= 1 


print("success rate is {}".format(successes/total))
#print kero_data
#print lox_data
#print helium_data

plt.plot(kero_data, 'b', label = 'Kero')
plt.plot(lox_data,'r',label = 'Lox')
plt.plot(helium_data,'g',label = "Helium")

plt.legend()
plt.grid()
plt.show()