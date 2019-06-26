#text input
from sklearn.feature_extraction.text import CountVectorizer

corpus=["Authman ran faster than Harry because Authman is real and Harry is fictional.",
		"Authman and Harry ran faster then faster and faster.",
		"W00t."		
]

bow=CountVectorizer()
x=bow.fit_transform(corpus)		#gives a sparse matrix
print(x)

print(bow.get_feature_names())	#print the words
print(x.toarray())		#helps to use the spares matrix in as array


#------------------------------------------------------------------------------
#image: 2d array of pixels
from scipy import misc		#import
img=misc.imread('eg.png')			#read image

print(type(img))			#returns the type of data
print(img.shape)			#returns the size 
print(img.dtype)			#data type of image

img=img[::2,::2]			#to reduce the correlation between two pixels next toeach other
print(img.shape) 			#shrinks the image
img=(img/255.).reshape(-1,4)		#red, green, blue, alpha
#reduce the image to 1d

#grayscale luminance formula is slightly diferent than a straight mean()
#science we are able to see many more shades of green than we are of red
red=img[:,0]
green=img[:,1]
blue=img[:,2]

gray = 0.299 * red + 0.587 * green + 0.114 * blue		#convert the image to grayscale
print(img.shape)		
print(gray.shape)

#------------------------------------------------------------------------------------
#audio: 1d sound wave
import scipy.io.wavfile as wavfile

sample_rate, audio_data= wavfile.read('bird.wav')		#read audio
print(sample_rate)		#gives the sample rate
print(audio_data)		#subset of the data