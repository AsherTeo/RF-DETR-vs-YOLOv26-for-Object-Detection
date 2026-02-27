## Introduction

YOLO-based detectors are widely used in object detection because of their real-time inference speed and strong accuracy. While transformer-based detectors have been proposed as alternatives, they typically introduce higher computational cost and slower inference. Recent developments such as RF-DETR demonstrate that transformer-based models can achieve high mAP while maintaining efficient inference speed. This project explores and compares the performance of RF-DETR and YOLOv26 across five datasets using a unified experimental setup.

## 2. Dataset

### 1) [Indoor Fire](https://www.kaggle.com/datasets/pengbo00/home-fire-dataset)

Classes: Fire, Smoke Training Data : 3900

Goal: Detect small fire regions in indoor environments for early fire detection.

### 2) [Aquarium](https://public.roboflow.com/object-detection/aquarium/2)

Classes : Jellyfish, Pengiun, Shark, Starfish, Stingary  Training Data : 449

Goal: Detect and distinguish aquatic species for educational and automatic counting applications.

### 3) [Floor Plans](https://www.kaggle.com/datasets/umairinayat/floor-plans-500-annotated-object-detection?select=data.yaml)

Classes : Door symbol, Window symbol, Zone  Training Data : 769

Goal: Detect architectural symbols for automatic CAD conversion (AutoCAD) and object counting.

### 4) [Entrance](https://www.kaggle.com/datasets/evanrantala/entrances-dataset-street-level-object-detection)

Classes : Entrance Training Data : 795

Goal: Detect building entrances in street scenes for navigation and delivery applications.

### 5) [Vertebra](https://www.kaggle.com/datasets/salmankey/scoliosis-yolov5-annotated-spine-x-ray-dataset)

Classes : Vertebra Training Data : 1536

Goal: Detect individual vertebrae to support Cobb angle estimation and scoliosis assessment.

## 3) Method

We trained both YOLOv26 and RF-DETR on the same training dataset using identical data splits.  

Both models were trained with an input resolution of 640 × 640 using the large (-L) variant of each architecture.  
Early stopping was applied during training to mitigate overfitting.

Due to differences in optimization behavior, different learning rates were used for the two models, with RF-DETR trained using a smaller learning rate to ensure stable convergence.

In addition, a 25-shot training configuration was evaluated to analyze model performance under limited data conditions.





