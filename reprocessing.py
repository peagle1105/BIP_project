import numpy as np
import cv2

#Global variable
image_folder = "E:/BrainTumorModelTraining/BrainTumorDataset"
meningioma_training_folder = "Training/meningioma"; notumor_training_folder = "Training/notumor"
meningioma_prefix = "Tr-me_"; notumor_prefix = "Tr-no_"
exten = ".jpg"

#Supporting function
def pepernoiseRemove()
#Main function