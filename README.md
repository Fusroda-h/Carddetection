# Card detection with YOLOv4-tiny
----
## 1. About our project
----
### 1.1. Project selection

We started a project for object detection with [jestson nano][jetson link] and we selected "card detection" as my project topic.
This was a project for my lecture <AIplatform> and we wanted to make an AI model familiar in our daily lives. Me and my team member liked playing card game and wanted to share the joy of playing card game who don’t know the rules. Also, we are living in the time of covid-19, so I thought the “Card game detection and scoring project” might help people to stay indoors.

### 1.2. Project objectives

We chose 3 objectives for my project.
First, realtime object detection speed of faster than 20 fps.
Second, model test accuracy for IOU=0.5  to exceed at least 90%, and real-time average accuracy of 80%.
Third, detecting each card and label the card set (of 5 cards) according to poker game scoring rules.

### 1.3. Model selection

We chose YOLOv4-tiny as my "Card-Detection model".
This is because YOLOv4 is slightly slower than ssd-mobilenetv2, more accurate than ssd-mobilenetv2.
So, we needed both fast and accurate model. We chose YOLOv4-tiny model as our model.

![yoloimg1](https://github.com/Fusroda-h/Carddetection/images/yolo_v4_vs_v3.jpg)
![yoloimg2](https://github.com/Fusroda-h/Carddetection/images/yolo_v3_vs_mob2.jpg)
----
## 2. Project Result
----
### 2.1. Training 

We got "playing card data set" from [okmd/playing-card-dataset][dataset].
We used 3000 data from dataset for training. Training was conducted in a google COLAB pro environment. We trained our model with 416*416 size, 16 batch, 8 subdivision, and learning rate of 0.00261.

### 2.2 Optimization

We use TensorRT to optimize our model. We convert darknet model to ONNX model and convert ONNX model to TensorRT engine. At first, we tried to use torch2trt module but did not work well. We found that darknet model changed to torch model might not work well for torch2trt module. So, we had to make darknet model to ONNX and change ONNX to TensorRT engine.
We made TensorRT engine out of our trained yolov4-tiny darknet model.
We build trt module in FP16.

### 2.3 Implementation

We refer to the git [jkjung-avt/tensorrt_demos][refer1].
We changed som code and customized the code to fit our model and we made our environment as docker image "gaimbler/carddetection". You can use this environment.

This is real-time test demo video of our model.

![Demo](https://github.com/Fusroda-h/Carddetection/images/PBL_final_demo.mp4)





 




----
* Junghwan Lee & Kwangsoo Seol proceeded this project.

----
###Reference
[jkjung-avt/tensorrt_demos][refer1]

[jetson link]:https://developer.nvidia.com/embedded/jetson-nano-developer-kit
[dataset]:https://github.com/okmd/playing-card-dataset 
[refer1]:https://github.com/jkjung-avt/tensorrt_demos