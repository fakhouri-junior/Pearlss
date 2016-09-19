import numpy as np
import PIL.Image
from scipy.misc import imread, imresize, imsave, imshow

def load_image(path, height, width, mode='RGB'):
    image = imread(path)
    image = imresize(image, (height,width))
    return image

# CHANGE THE PATH IF YOU WANT TO USE IT AND DELETE THOSE
image = load_image('/home/salim/bassam/external.jpg',400,760)
imsave('/home/salim/bassam/external760.jpg',image)








