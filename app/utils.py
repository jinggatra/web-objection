# Mask-RCNN Imports
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from PIL import Image 
# Matplotlib Import
import matplotlib.pyplot as plt
import os
import sys
import random
import math
import re
import time
import numpy as np
import tensorflow as tf
import matplotlib
import mrcnn.model as modellib
import matplotlib.patches as patches

class PredictionConfig(Config):
    # define the name of the configuration
    NAME = "website"
    # number of classes (background + kangaroo)
    NUM_CLASSES = 1 + 6
    # number of training steps per epoch
    GPU_COUNT = 1
    IMAGE_SHAPE = [1920, 1080, 3]
    # DETECTION_MIN_CONFIDENCE = 0.7
    IMAGES_PER_GPU = 1

config = PredictionConfig()

class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()
DEVICE = "/gpu:0"  # /cpu:0 or /gpu:0
model_path = 'model/mask_rcnn_website_0020.h5'

with tf.device(DEVICE):
    model = modellib.MaskRCNN(mode="inference", model_dir=model_path,
                              config=config)

# load model weights
model.load_weights(model_path, by_name=True)
print('Model Loaded Successfully!!')
model.keras_model.make_predict_function()


def model_predict(img_path):
        # image = load_img(img_path)
        # image = img_to_array(image)
        image = plt.imread(img_path)
        if image.shape[-1] == 4:
            image = image[..., :3]
                
        results = model.detect([image], verbose=1)
        return results