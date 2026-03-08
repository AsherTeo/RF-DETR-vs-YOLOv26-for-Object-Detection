## Acknowledgement
This project is based on the implementation of
- [YOLO 26](https://github.com/ultralytics/ultralytics)
- [RF DETR](https://github.com/roboflow/rf-detr)

We thank the original authors and contributors for making their work publicly available.

## Installation
This project builds upon the original implementations.
For environment setup and dependencies, please follow the installation instructions provided in the respective repositories.

## 1. Introduction

YOLO-based detectors are widely adopted in object detection due to their real-time inference speed and strong detection accuracy. Although transformer-based detectors have been proposed as alternatives, they often introduce higher computational cost and slower inference, which limits their practical deployment in real-world systems.

Recent developments such as RF-DETR demonstrate that transformer-based architectures can attain competitive mean Average Precision (mAP) while preserving efficient inference speed. This is accomplished through the use of Neural Architecture Search (NAS) with DINOv2 and deformable cross-attention in place of standard cross-attention, thereby significantly reducing inference time complexity. This raises the question of whether transformer-based detectors can outperform YOLO-based models under standard training conditions across different datasets.

In this project, we compare the performance of RF-DETR and YOLO 26 on five object detection datasets using a unified experimental setup. Both models are trained and evaluated under identical data splits and image resolutions to ensure a fair comparison. Performance is assessed using standard object detection metrics, including precision, recall, and mean Average Precision (mAP).

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

We trained both YOLO 26 and RF-DETR on the same training dataset using identical data splits.

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

| Ground Truth | YOLOv26 | RF-DETR |
|-------------|---------|---------|
| ![GT_1](https://github.com/user-attachments/assets/67a17f28-d042-4af1-9388-76940d63378f) | ![YOLO_1](https://github.com/user-attachments/assets/0264400b-7d0c-44f5-a8b1-93eb1b9475ab) | ![RF_1](https://github.com/user-attachments/assets/4a2d3fcd-8a28-4ba8-a113-498ca11151a3) |
| ![GT_3](https://github.com/user-attachments/assets/7bfbb96b-4956-47dc-8165-c1e2c5f3c066) | ![YOLO_3](https://github.com/user-attachments/assets/3851a5e1-89fc-41f1-abcd-78e9fe3174aa) | ![RF_3](https://github.com/user-attachments/assets/50387c94-9dca-42a1-982b-73ce3f965025) |

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

| Ground Truth | YOLOv26 | RF-DETR |
|-------------|---------|---------|
| ![GT_1](https://github.com/user-attachments/assets/d6b8acb3-b835-46c2-8366-bae3dc92df9e) | ![YOLO_1](https://github.com/user-attachments/assets/ec24e893-5178-4158-b7d6-655d67118923) | ![RF_1](https://github.com/user-attachments/assets/fdc0fbad-b864-4ffe-aed9-9bbb4dbaab98) |
| ![GT_2](https://github.com/user-attachments/assets/d37b1fa8-28ae-48f1-967a-a8e1f01c5a75) | ![YOLO_2](https://github.com/user-attachments/assets/3a28e074-9bd0-4233-93ae-315a4a02ddb2) | ![RF_2](https://github.com/user-attachments/assets/524f8e76-4aae-40b9-a7c7-a27b32ddf2f8) |

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

### YOLOv26
**Pros**
- Supports many data augmentation techniques (e.g., Mosaic, CutMix), which help improve model performance.
- Highly optimized and widely used, making both training and inference efficient.
- Faster training compared to transformer-based detectors.
- Large community support and extensive documentation, making troubleshooting easier.
- Achieves higher mAP compared to RF-DETR across most datasets.
- Does not require large amounts of GPU VRAM.

**Cons**
- Requires a larger amount of training data to achieve robust performance.
- Recall is generally lower than RF-DETR, particularly in few-shot settings.
- Small objects (fire) may be harder to detect compared to RF-DETR.


### RF-DETR
**Pros**
- Performs better with smaller training datasets compared to YOLO 26, especially in terms of recall.
- Achieves higher recall compared to YOLO 26 across most datasets.
- Converges in fewer epochs, requiring less training time to reach stable performance.
- Better detection performance for small objects (e.g., fire).
- 
**Cons:**
- Requires a large amount of GPU VRAM due to the transformer-based architecture.  
- Achieves worse mAP compared to YOLOv26 in most experiments.  
- Data augmentation techniques such as Mosaic may not improve performance, since RF-DETR relies on global self-attention rather than local receptive fields.  
- Limited community resources and fewer troubleshooting examples compared to YOLO-based models.

## 6. Inference 

## Inference Results

We tested **7 fire videos** using YOLO 26 and RF-DETR with inference on an **RTX 5070 Ti** GPU.  
The table below reports the average performance across all test videos.

| Model | Average Latency (ms) | Inference FPS |
|------|----------------------|---------------|
| YOLOv26 | 22.85 | 43.77 |
| RF-DETR | 21.74 | 46.01 |

## Video Results

Below are example inference results comparing YOLOv26 and RF-DETR on fire detection videos.

Comparison Video 1 
https://youtu.be/p8WVWJ38CXw  

Comparison Video 2
https://youtu.be/ph1d436xnvY  

Comparison Video 3
https://youtu.be/j7KvUfRjH3w

## 7. Conclusion

- Across five datasets, RF-DETR achieves higher recall and performs better when detecting small objects such as fire.

- YOLO 26 achieves higher mAP, indicating more precise object localization with tighter bounding boxes. 

- Overall, both models show strong performance with different strengths depending on the detection requirements.
