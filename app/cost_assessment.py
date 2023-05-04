import cv2
import numpy as np

def class_name(classid):
    id_dict = {1:'Text Field', 2:'Image', 3:'Button', 4:'Menu Bar', 5:'Side Bar', 6:'Nav Bar'}
    return id_dict[classid]

# def ct_out(classid):
#     # cost_dict = {1: [800, 1400], 2:[1200, 3000],3:19000, 4:17000}
#     cost_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}

#     return cost_dict[classid]

def tp_out(classid):
    # cost_dict = {1: [800, 1400], 2:[1200, 3000],3:19000, 4:17000}
    # tp_dict = {1: 'tf.read()', 2:'bt.read()', 3:'img.read()', 4:'mb.read()', 5:'sb.read()', 6:'nb.read()'}
    tp_dict = {1: '<form action=###><label for="fname">First name:</label><input type="text" id="fname" name="fname"></form>', 
                2:'<img src="###" alt="###" width="###" height="###">', 
                3:'<button type="button">button</button>', 
                4:'<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>',
                5:'<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>', 
                6:'<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>'}
    return tp_dict[classid]
    
def area_ratio(image, roi, mask):
    y1, x1, y2, x2 =  tuple(roi)
    crop_mask = mask[y1:y1+(y2-y1),x1:x1+(x2-x1)].copy()
    pixels = cv2.countNonZero(np.float32(crop_mask))
    image_area = image.shape[0] * image.shape[1]
    area_ratio = 1 + (pixels / image_area)
    return area_ratio

def costEstimate(image, rois, masks, classids):
    cost_id_dict = {
    "Text Field": {"Count": 0, "Temp": '<form action=###><label for="fname">First name:</label><input type="text" id="fname" name="fname"></form>'},
    "Image": {"Count": 0, "Temp": '<img src="###" alt="###" width="###" height="###">'},
    "Button": {"Count": 0, "Temp": '<button type="button">button</button>'},
    "Menu Bar": {"Count": 0, "Temp": '<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>'},
    "Side Bar": {"Count": 0, "Temp": '<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>'},
    "Nav Bar": {"Count": 0, "Temp": '<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>'}
    }
    count = int()
    template = ''
    for index in range(rois.shape[0]):

        name = class_name(classids[index])
        temp = tp_out(classids[index])
        ratio = area_ratio(image, rois[index], masks[: ,: ,index])
        print(classids)
        print(temp)
        
        if name == 'Text Field':
            count = cost_id_dict[name]['Count'] + 1
            cost_id_dict[name]['Count'] = count
            template = cost_id_dict[name]['Temp']
        elif name == 'Image':
            count = cost_id_dict[name]['Count'] + 1
            cost_id_dict[name]['Count'] = count
            template = cost_id_dict[name]['Temp']
        elif name == 'Button':
            count = cost_id_dict[name]['Count'] + 1
            cost_id_dict[name]['Count'] = count
            template = cost_id_dict[name]['Temp']
        elif name == 'Menu Bar':
            count = cost_id_dict[name]['Count'] + 1
            cost_id_dict[name]['Count'] = count
            template = cost_id_dict[name]['Temp']
        elif name == 'Side Bar':
            count = cost_id_dict[name]['Count'] + 1
            cost_id_dict[name]['Count'] = count
            template = cost_id_dict[name]['Temp']
        else:
            count = cost_id_dict[name]['Count'] + 1
            cost_id_dict[name]['Count'] = count
            template = cost_id_dict[name]['Temp']

    for name, values in cost_id_dict.copy().items():
        if values['Count'] == 0:
            cost_id_dict.pop(name)
            # cost_id_dict.pop(temp)

    return template, cost_id_dict
    
# raise KeyError(message)
    # cost_id_dict = {
    # "Text Field": {"Count": 0, "T": '<form action=###><label for="fname">First name:</label><input type="text" id="fname" name="fname"></form>'},
    # "Image": {"Count": 0, "T": '<img src="###" alt="###" width="###" height="###">'},
    # "Button": {"Count": 0, "T": '<button type="button">button</button>'},
    # "Menu Bar": {"Count": 0, "T": '<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>'},
    # "Side Bar": {"Count": 0, "T": '<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>'},
    # "Nav Bar": {"Count": 0, "T": '<ul><li><a href="###">###</a></li><li><a href="###">###</a></li></ul>'}
    # }
    
            # elif name == 'Nav Bar':
            # count = cost_id_dict[name]['Count'] + 1
            # cost_id_dict[name]['Count'] = count
            # template = cost_id_dict[name]['Cost']