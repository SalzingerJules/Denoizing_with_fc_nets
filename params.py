#IMPORTS
from keras import losses
from keras import optimizers

#_____DATA PARAMETERS_____

image_number_dft = 5000
noise_type_dft = 'gaussian'
stdd_dft = 0.01
shape_dft = (64,64,1)


#_____DEFAULT TRAINING PARAMETERS_____

epochs_dft = 30
batch_size_dft = 32
ctc_name_dft = 'denoiser_1_ctc'
ntc_name_dft = 'denoiser_1_ntc'
flatten_dft = True


#_____DEFAULT NET PARAMETERS_____

learning_rate_dft = 0.001
loss_dft = losses.mean_squared_error
optimizer_dft = optimizers.Adam(lr = learning_rate_dft)
