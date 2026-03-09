import os
import json

def add_superclass(path, super_name):
    label_path = os.path.join(path, '_annotations.coco.json')
    save_path = os.path.join(path, '_annotations.coco.json')

    super_class = [{
                    "id": 0,
                    "name": f'{super_name}',
                    "supercategory": "none"
                    }]
    new_cat = []

    with open(label_path, 'r') as file:
        coco = json.load(file)

        for cat in coco['categories']:
            cat['id'] += 1
            cat['supercategory'] = f'{super_name}'
        
        new_cat.extend(super_class)
        new_cat.extend(coco['categories'])

        coco['categories'] = new_cat 

        for anno in coco['annotations']:
            anno['category_id'] += 1

    with open(save_path, 'w') as filess:
        json.dump(coco, filess, indent = 4)

def remove_label(all, dataset, cls_excluded = None, new_label_mapping = None):
    path = rf'C:\rf-detr\{dataset}\{all}\_annotations.coco.json'
    save_path = rf'C:\rf-detr\{dataset}\{all}\_annotations.coco.json'

    if dataset == 'aquarium_data':
        cls_excluded = {1: 'fish', 4:'puffin'}
        new_label_mapping = {0:0, 2:1, 3:2, 5:3, 6: 4, 7:5}

    else:
        cls_excluded = cls_excluded
        new_label_mapping = new_label_mapping
        
    new_cat = []
    new_anno = []

    with open(path, 'r') as file:
        coco = json.load(file)

    for cat in coco['categories']:
        if cat['id'] not in cls_excluded:
            new_cat.append(cat)

    for cat in new_cat:
        cat['id'] = new_label_mapping[cat['id']]

    for anno in coco['annotations']:
        if anno['category_id'] not in cls_excluded:
            new_anno.append(anno)

    for anno in new_anno:
        anno['category_id'] = new_label_mapping[anno['category_id']]

    new_coco = {
        'categories': new_cat,
        'images': coco['images'],
        'annotations': new_anno,

    }

    with open(save_path, 'w') as filess:
        json.dump(new_coco, filess, indent = 4)