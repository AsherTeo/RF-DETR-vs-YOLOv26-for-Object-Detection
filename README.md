## 1. Introduction

YOLO-based detectors are widely adopted in object detection due to their real-time inference speed and strong detection accuracy. Although transformer-based detectors have been proposed as alternatives, they often introduce higher computational cost and slower inference, which limits their practical deployment in real-world systems.

Recent developments such as RF-DETR demonstrate that transformer-based architectures can attain competitive mean Average Precision (mAP) while preserving efficient inference speed. This is accomplished through the use of Neural Architecture Search (NAS) with DINOv2 and deformable cross-attention in place of standard cross-attention, thereby significantly reducing inference time complexity. This raises the question of whether transformer-based detectors can outperform YOLO-based models under standard training conditions across different datasets.

In this project, we compare the performance of RF-DETR and YOLOv26 on five object detection datasets using a unified experimental setup. Both models are trained and evaluated under identical data splits and image resolutions to ensure a fair comparison. Performance is assessed using standard object detection metrics, including precision, recall, and mean Average Precision (mAP).

Through this study, we aim to analyze the strengths and weaknesses of each model and provide insights into their behavior across different datasets and training conditions.

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

## 3. Method

We trained both YOLOv26 and RF-DETR on the same training dataset using identical data splits.

Both models were trained with an input resolution of 640 × 640 using the large (-L) variant of each architecture. Early stopping was applied during training to mitigate overfitting.

Due to differences in optimization behavior, different learning rates were used for the two models: YOLOv26 was trained with a learning rate of 0.001, while RF-DETR was trained with a smaller learning rate of 0.0001 to ensure stable convergence.

For evaluation, the confidence threshold was fixed at 0.2 for both YOLOv26 and RF-DETR to ensure a fair comparison.

In addition, a 25-shot training configuration was evaluated to analyze model performance under limited data conditions.

## 4. Results

### Indoor Fire

| Ground Truth | YOLOv26 | RF-DETR |
|-------------|---------|---------|
| ![test_920](https://github.com/user-attachments/assets/3a17d83e-4650-4c91-8c8b-ed584a40d3ea) | ![test_920_yolo](https://github.com/user-attachments/assets/c1e9c818-55d3-4c55-a74b-74a63fd1a396) | ![test_920_rfdetr](https://github.com/user-attachments/assets/59b63559-2423-4779-8167-fd7320cd1b3d) |
| ![test_496](https://github.com/user-attachments/assets/9c988541-38ec-4067-9a40-f7fe8f29acff) | ![test_496_rfdetr](https://github.com/user-attachments/assets/0c9544c1-6703-49d6-b49f-6b8de41e29e7) | ![test_496_yolo](https://github.com/user-attachments/assets/19f2bc12-e9a0-44ed-ad22-74dc28a0825f) | 


| Model   | Setting      | Epochs | Precision | Recall | mAP@50 | mAP@50–95 |
|---------|--------------|--------|-----------|--------|--------|-----------|
| YOLO 26 | All Data     | 100    | 0.957     | 0.923  | 0.950  | 0.731     |
| RF-DETR | All Data     | 40     | 0.959     | **0.950**  | 0.940  | 0.675     |
| YOLO 26 | 25 Few-Shot  | 200    | 0.872     | 0.474  | 0.674  | 0.448     |
| RF-DETR | 25 Few-Shot  | 82     | 0.831     | 0.734  | 0.695  | 0.428     |

### Aquarium

| Model   | Setting      | Epochs | Precision | Recall | mAP@50 | mAP@50–95 |
|---------|--------------|--------|-----------|--------|--------|-----------|
| YOLO 26 | All Data     | 58     | 0.881     | 0.743  | 0.818  | 0.610     |
| RF-DETR | All Data     | 54     | 0.891     | 0.814  | 0.780  | 0.556     |
| YOLO 26 | 25 Few-Shot  | 105    | 0.792     | 0.631  | 0.720  | 0.536     |
| RF-DETR | 25 Few-Shot  | 74     | 0.844     | 0.731  | 0.681  | 0.484     |

### Floor Plans

| Ground Truth | YOLOv26 | RF-DETR |
|-------------|---------|---------|
|![975_png rf 4ad67b65bf1f6a06d16fddfea5a7a6fe](https://github.com/user-attachments/assets/efdc6f31-2e13-4b87-b231-e65c7233fcea)|![975_png rf 4ad67b65bf1f6a06d16fddfea5a7a6fe](https://github.com/user-attachments/assets/d82768ff-9dca-4c38-9328-61d772a4dd81)|![975_png rf 4ad67b65bf1f6a06d16fddfea5a7a6fe](https://github.com/user-attachments/assets/301da656-c427-43ee-94a1-7d81990ba095)|


| Model   | Setting      | Epochs | Precision | Recall | mAP@50 | mAP@50–95 |
|---------|--------------|--------|-----------|--------|--------|-----------|
| YOLO 26 | All Data     | 78     | 0.875     | 0.809  | 0.852  | 0.584     |
| RF-DETR | All Data     | 56     | 0.881     | 0.844  | 0.802  | 0.522     |
| YOLO 26 | 25 Few-Shot  | 133    | 0.851     | 0.640  | 0.750  | 0.500     |
| RF-DETR | 25 Few-Shot  | 50     | 0.838     | 0.747  | 0.699  | 0.437     |

### Entrance

| Model   | Setting      | Epochs | Precision | Recall | mAP@50 | mAP@50–95 |
|---------|--------------|--------|-----------|--------|--------|-----------|
| YOLO 26 | All Data     | 100    | 0.750     | 0.483  | 0.650  | 0.448     |
| RF-DETR | All Data     | 34     | 0.750     | 0.621  | 0.591  | 0.395     |
| YOLO 26 | 25 Few-Shot  | 32     | **1.000** | 0.0345 | 0.517  | 0.259     |
| RF-DETR | 25 Few-Shot  | 78     | 0.684     | 0.448  | 0.350  | 0.218     |

### Vertebra

| Ground Truth | YOLOv26 | RF-DETR |
|-------------|---------|---------|
| ![GT](https://github.com/user-attachments/assets/9c386525-a346-45ef-a4c4-c3c153a42070) | ![YOLOv26](https://github.com/user-attachments/assets/dc2b0bab-31d1-44cd-a4d7-b49485164ed5) | ![RF-DETR](https://github.com/user-attachments/assets/ae4e9588-29e4-4ec9-8a5e-aa55cbab097e) |


| Model   | Setting      | Epochs | Precision | Recall | mAP@50 | mAP@50–95 |
|---------|--------------|--------|-----------|--------|--------|-----------|
| YOLO 26 | All Data     | 65     | 0.931     | 0.919  | 0.934  | 0.600     |
| RF-DETR | All Data     | 58     | 0.933     | **0.934** | 0.920  | 0.539     |
| YOLO 26 | 25 Few-Shot  | 120    | 0.911     | 0.822  | 0.883  | 0.519     |
| RF-DETR | 25 Few-Shot  | 100    | 0.879     | 0.884  | 0.857  | 0.423     |

## 5. Pros and Cons

### YOLO 26  
**Pros:**
- Supports many data augmentation (e.g., Mosaic, CutMix), which helps optimize model performance.  
- Highly optimized and widely used, making training and inference efficient.  
- Faster training compared to transformer-based detectors.  
- Large community and extensive documentation, so errors and issues are easier to troubleshoot.  
- Achieves better mAP compared to RF-DETR across most datasets.
- Does not require a large amount of GPU VRAM

**Cons:**
- Requires a larger amount of training data to become robust
- Recall performance is generally lower than RF-DETR, particularly in few-shot settings.

### RF-DETR  
**Pros:**
- Does not require a large amount of training data to become robust, especially in terms of recall.  
- Achieves higher recall compared to YOLOv26 across most datasets.  
- Converges in fewer epochs, requiring less training time to reach stable performance.

**Cons:**
- Requires a large amount of GPU VRAM due to the transformer-based architecture.  
- Achieves worse mAP compared to YOLOv26 in most experiments.  
- Data augmentation techniques such as Mosaic may not improve performance, since RF-DETR relies on global self-attention rather than local receptive fields.  
- Limited community resources and fewer troubleshooting examples compared to YOLO-based models.

## 6. Conclusion

- 
