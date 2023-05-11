# Basic System Imports
import os
import matplotlib.pyplot as plt
from PIL import Image
from mrcnn.utils import Dataset
# Flask Import
from flask import render_template, request, Flask, url_for
from os import listdir
# class that defines and loads the kangaroo dataset
class KangarooDataset(Dataset):
	# load the dataset definitions
	def load_dataset(self, dataset_dir, is_train=True):
		# define one class
		self.add_class("dataset", 1, "Text Field")
		self.add_class("dataset", 2, "Image")
		self.add_class("dataset", 3, "Button")
		self.add_class("dataset", 4, "Menu Bar")
		self.add_class("dataset", 5, "Side Bar")
		self.add_class("dataset", 6, "Nav Bar")
		# define data locations
		images_dir = dataset_dir +'/dataset/test/'
		annotations_dir = dataset_dir + '/data/anotation/'
		# find all images
		for filename in listdir(images_dir):
			# extract image id
			image_id = filename[:-4]
			# skip bad images
			if image_id in ['00090']:
				continue
			# skip all images after 150 if we are building the train set
			if is_train and int(image_id) >= 119:
				continue
			# skip all images before 150 if we are building the test/val set
			if not is_train and int(image_id) < 119:
				continue
			img_path = images_dir + filename
			ann_path = annotations_dir + image_id + '.xml'
			# add to dataset
			self.add_image('dataset', image_id=image_id, path=img_path, annotation=ann_path)


dataset = KangarooDataset()

# Must call before using the dataset
dataset.prepare()

print("Images: {}\nClasses: {}".format(len(dataset.image_ids), dataset.class_names))

def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

# Model Import
from app.utils import model_predict

from app.utils import config

# Cost Asssessment Import
from app import cost_assessment

# Mask-RCNN Import
from mrcnn import visualize

UPLOAD_PATH = 'static/uploads/'
UPLOAD_PRED_PATH = 'static/prediction/'

def base():
	return render_template('base.html')

def index():
	return render_template('index.html')
	
def websiteapp():
	return render_template('websiteapp.html')

def getwidth(path):
	img = Image.open(path)
	size = img.size # width and height
	aspect = size[0]/size[1] # width / height
	w = 300 * aspect
	return int(w)

def website():
	fileupload = False
	cost_for_damage = True
	if request.method == 'POST':
		# File Upload
		fileupload=True
		f = request.files['fileToUpload']
		if not os.path.exists(os.path.join(UPLOAD_PATH, f.filename.split('.')[0])):
			os.mkdir(os.path.join(UPLOAD_PATH, f.filename.split('.')[0]))

		image_path = f.filename.split('.')[0] + '/' + f.filename

		# print(UPLOAD_PATH + image_path)

		f.save(UPLOAD_PATH + image_path)

		# print(f'File saved Successfully @ {image_path}')

		# Class Prediction
		results = model_predict(UPLOAD_PATH + image_path)

		class_names = ['BG', 'Text Field', 'Image', 'Button', 'Menu Bar', 'Side Bar', 'Nav Bar']
		ax = get_ax(1)
		r = results[0]

		image = plt.imread(UPLOAD_PATH + image_path)
		# image = load_img(UPLOAD_PATH + image_path)da
		# image = img_to_array(image)

		if not os.path.exists(UPLOAD_PRED_PATH + f.filename.split('.')[0]):
			os.mkdir(os.path.join(UPLOAD_PRED_PATH, f.filename.split('.')[0]))

		pred_path = UPLOAD_PRED_PATH + f.filename.split('.')[0]


		# def get_images_ids():
		# 	images_ids = Image.objects.values_list('id')
		# 	print(images_ids)
		# 	return images_ids
		
		# image_id =int(f.filename[:-4])
		# print(image_id)
		# image, image_meta, gt_class_id, gt_bbox, gt_mask =\
		# 	modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)

		# Save Predicted Class Image
		visualize.save_instances(image, r['rois'], r['masks'], r['class_ids'], class_names,  r['scores'], path=pred_path + '/' + f.filename)
		get_masks_filenames = visualize.get_masks(image, r['masks'], r['rois'], class_names, r['class_ids'], path=pred_path + '/')
		top_masks_filenames = visualize.display_top_masks_edit(image, r['masks'], r['class_ids'], class_names, path=pred_path + '/')
		get_roi_filenames = visualize.get_rois(image, r['rois'], path=pred_path + '/')
		# visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
        #                     dataset.class_names, r['scores'], ax=ax,
        #                     title="Predictions")
		if cost_for_damage:
			template, temp = cost_assessment.costEstimate(image, r['rois'], r['masks'], r['class_ids'])
			print(f'File Successfully Manipulated @ {pred_path}')
			data = {
			'visualize': f.filename.split('.')[0] + '/' + f.filename,
			'width': getwidth(UPLOAD_PATH + f.filename.split('.')[0] + '/' + f.filename),
			'masks': get_masks_filenames,
			'top_masks': top_masks_filenames,
			'roi': get_roi_filenames,
			'temp' : temp,
			'template' : template
			}
			return	render_template('website.html', pagename='Web Component Detection', fileupload=fileupload, data=data, cost_for_damage=cost_for_damage)
		else:
			data = {
			'visualize': f.filename.split('.')[0] + '/' + f.filename,
			'width': getwidth(UPLOAD_PATH + f.filename.split('.')[0] + '/' + f.filename),
			'masks': get_masks_filenames,
			'top_masks': top_masks_filenames,
			'roi': get_roi_filenames,
			}
			return	render_template('website.html', pagename='Web Component Detection', fileupload=fileupload, data=data, cost_for_damage=cost_for_damage)




		return render_template('website.html', pagename='Web Component Detection', fileupload=fileupload, data=data, cost_for_damage=cost_for_damage)
	return render_template('website.html', pagename='Web Component Detection', fileupload=fileupload)
