import numpy as np
import PIL.Image
from scipy.misc import imread, imresize, imsave, imshow

def load_image(path, height, width, mode='RGB'):
    image = imread(path)
    image = imresize(image, (height,width))
    return image

# CHANGE THE PATH IF YOU WANT TO USE IT AND DELETE THOSE
image = load_image('/home/salim/bassam/completed/mussafah.jpg',300,370)
imsave('/home/salim/bassam/completed/mussafah300.jpg',image)


image = load_image('/home/salim/bassam/completed/saadiyat.jpg',300,370)
imsave('/home/salim/bassam/completed/saadiyat300.jpg',image)



image = load_image('/home/salim/bassam/completed/tourist.jpg',300,370)
imsave('/home/salim/bassam/completed/tourist300.jpg',image)








