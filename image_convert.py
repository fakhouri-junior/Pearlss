import numpy as np
import PIL.Image
from scipy.misc import imread, imresize, imsave, imshow

def load_image(path, height, width, mode='RGB'):
    image = imread(path)
    image = imresize(image, (height,width))
    return image

# CHANGE THE PATH IF YOU WANT TO USE IT AND DELETE THOSE
image = load_image('/home/salim/bassam/in-hands/adac.jpg',300,370)
imsave('/home/salim/bassam/in-hands/adac300.jpg',image)

image = load_image('/home/salim/bassam/in-hands/central.jpg',300,370)
imsave('/home/salim/bassam/in-hands/central300.jpg',image)

image = load_image('/home/salim/bassam/in-hands/adac.jpg',300,370)
imsave('/home/salim/bassam/in-hands/adac300.jpg',image)

image = load_image('/home/salim/bassam/in-hands/mafraq_main.jpg',300,370)
imsave('/home/salim/bassam/in-hands/mafraq_main300.jpg',image)

image = load_image('/home/salim/bassam/in-hands/future.jpg',300,370)
imsave('/home/salim/bassam/in-hands/future300.jpg',image)

image = load_image('/home/salim/bassam/in-hands/saraya.jpg',300,370)
imsave('/home/salim/bassam/in-hands/saraya300.jpg',image)







