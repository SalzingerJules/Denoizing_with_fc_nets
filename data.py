#IMPORTS
from PIL import Image
import numpy as np
import os
import random as rd

import params


#PARAMETERS
default_image_number = params.image_number_dft
default_noise_type = params.noise_type_dft
default_stdd = params.stdd_dft
default_shape = params.shape_dft


#LOAD DATA
def open_images(file_name,
                image_number = default_image_number,
                image_shape = default_shape):
    os.chdir(file_name)
    folder_length = []
    folders = os.listdir()
    for i in folders:
        folder_length.append(len([k for k in os.listdir(i) if k.endswith('.jpg')]))
    samples = rd.sample([i for i in range(sum(folder_length))],image_number)
    array = np.zeros((image_number,image_shape[0],image_shape[1],image_shape[2]))
    for nb,i in enumerate(samples):
        path = ""
        for j in range(1,len(folders)+1):
            if i<sum(folder_length[:j]):
                path+=folders[j-1]+"/"+[k for k in os.listdir("./"+folders[j-1]) if k.endswith('.jpg')][i-sum(folder_length[:j-1])]
                break
        img = Image.open(path).convert('L')
        x1 = rd.randint(0,img.size[0]-65)
        y1 = rd.randint(0,img.size[1]-65)
        img = img.crop((x1,y1,x1+image_shape[0],y1+image_shape[1]))
        array[nb] = np.reshape(np.asarray(img).astype(np.float32)/255,(image_shape[0],image_shape[1],image_shape[2]))
        if nb/(image_number//100) == nb//(image_number//100):
            print("Loading database... "+str(nb//(image_number//100))+"%.")
    return array


#ADD NOISE TO DATA
def add_noise(array,
              noise_type = default_noise_type,
              stdd = default_stdd,
              image_number = default_image_number,
              image_shape = default_shape):
    if noise_type == 'gaussian':
        return np.add(array,np.random.normal(0,stdd,(image_number,image_shape[0],image_shape[1],image_shape[2])))


