import numpy as np
import cv2

#Global variable
image_folder = "E:/BrainTumorModelTraining/BrainTumorDataset"
meningioma_training_folder = "Training/meningioma"; notumor_training_folder = "Training/notumor"
meningioma_prefix = "Tr-me_"; notumor_prefix = "Tr-no_"
exten = ".jpg"

#Supporting function
def pepernoiseRemove(image_path, contrast_factor):
    # Load the image
    image = cv2.imread(image_path)
    alpha = contrast_factor
    beta = 0
    # Apply the contrast adjustment
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
# Example usage
pepernoiseRemove('jpg', 1.5)
#Main function
