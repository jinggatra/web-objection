# Mask-RCNN Imports
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from PIL import Image 
# Matplotlib Import
import matplotlib.pyplot as plt

class PredictionConfig(Config):
    # define the name of the configuration
    NAME = "website"
    # number of classes (background + kangaroo)
    NUM_CLASSES = 1 + 6
    # number of training steps per epoch
    GPU_COUNT = 1
    IMAGE_SHAPE = [1920, 1080, 3]
    DETECTION_MIN_CONFIDENCE = 0.40
    IMAGES_PER_GPU = 1


cfg = PredictionConfig()
# define the model
cfg.display()
model = MaskRCNN(mode='inference', model_dir='./', config=cfg)
# load model weights
model_path = 'model/mask_rcnn_website_0020.h5'
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