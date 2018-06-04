#IMPORTS
from keras.layers import Dense,Conv2D,Multiply,Concatenate,Input,Dropout,Flatten
from keras.models import Model
from keras.optimizers import Adam
import numpy as np

import regularizers
import params


#PARAMETERS
default_loss = params.loss_dft
default_optimizer = params.optimizer_dft
default_shape = params.shape_dft
default_epochs = params.epochs_dft
default_batch_size = params.batch_size_dft
default_image_number = params.image_number_dft
default_ctc_name = params.ctc_name_dft
default_ntc_name = params.ntc_name_dft
default_flatten = params.flatten_dft


#MODEL
def denoiser(shape = default_shape,
             loss = default_loss,
             optimizer = default_optimizer,
             multi_scale_dropout = 0,
             load = False,
             load_name = '',
             flatten = False):
    image_input = Input(shape=shape,name='d_input')

    ms_1 = Conv2D(32,(1,1),padding='same',activation='relu',name='d1_l1_1')(image_input)
    ms_3 = Conv2D(40,(3,3),padding='same',activation='relu',name='d1_l1_3')(image_input)
    ms_5 = Conv2D(48,(5,5),padding='same',activation='relu',name='d1_l1_5')(image_input)
    ms_7 = Conv2D(56,(7,7),padding='same',activation='relu',name='d1_l1_7')(image_input)
    ms_9 = Conv2D(64,(9,9),padding='same',activation='relu',name='d1_l1_9')(image_input)
    multi_scale_total = Concatenate(3)([ms_1,ms_3,ms_5,ms_7,ms_9])
    multi_scale_dropout = Dropout(multi_scale_dropout)(multi_scale_total)

    denoising_layer_1 = Conv2D(240,(3,3),padding='same',activation='relu',name='d1_l2_1')(multi_scale_dropout)
    denoising_layer_2 = Conv2D(240,(1,1),padding='same',activation='relu',name='d1_l2_2')(denoising_layer_1)
    denoising_layer_3 = Conv2D(240,(1,1),padding='same',activation='sigmoid',name='d1_l2_3')(denoising_layer_2)

    hadamard = Multiply()([denoising_layer_3,multi_scale_total])

    reconstruction_layer_1 = Conv2D(64,(3,3),padding='same',kernel_regularizer = regularizers.lp(),activation='relu',name='d1_l3_1')(hadamard)
    reconstruction_layer_2 = Conv2D(32,(1,1),padding='same',kernel_regularizer = regularizers.lp(),activation='relu',name='d1_l3_2')(reconstruction_layer_1)
    reconstruction_layer_3 = Conv2D(1,(1,1),padding='same',activation='sigmoid',name='d1_l3_3')(reconstruction_layer_2)

    output_layer = Flatten()(reconstruction_layer_3)
    if flatten:
        denoiser = Model(input=image_input,output=output_layer)
    else:
        denoiser = Model(input=image_input,output=reconstruction_layer_3)
    denoiser.compile(loss = loss, optimizer = optimizer,metrics=['accuracy'])
    if load:
        denoiser.load_weights(load_name)
    return denoiser


#TRAININGS
def train_clean_to_clean(xtrain,
                         epochs = default_epochs,
                         batch_size = default_batch_size,
                         save_name = default_ctc_name,
                         image_number = default_image_number,
                         flatten = default_flatten,
                         verbose = 1):
    if flatten:
        labels = np.zeros((image_number,4096))
        for i in range(image_number):
            labels[i]=np.reshape(xtrain[i],(4096,))
    else:
        labels = ytrain[:]
    denoiser_1 = denoiser(shape=default_shape,multi_scale_dropout=0.7,flatten=flatten)
    history = denoiser_1.fit(xtrain,labels,epochs=30,batch_size=32,verbose=verbose)
    denoiser.save(save_name)
    return history


def train_noisy_to_clean(xtrain,ytrain,
                         epochs = default_epochs,
                         batch_size = default_batch_size,
                         save_name = default_ntc_name,
                         load_name = default_ctc_name,
                         flatten = default_flatten,
                         verbose = 1):
    if flatten:
        labels = np.zeros((image_number,4096))
        for i in range(image_number):
            labels[i]=np.reshape(ytrain[i],(4096,))
    else:
        labels = ytrain[:]
    denoiser_1 = denoiser(shape=default_shape,load=True,load_name=load_name,flatten=flatten)
    history = denoiser_1.fit(xtrain,labels,epochs=epochs,batch_size=batch_size,verbose=verbose)
    denoiser.save(save_name)
    return history
