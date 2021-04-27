# FACE RECOGNITION WITH FACENET


### 1.install  dependencies
```
$ python3 -m venv name-of-venv
$ source name-of-venv/bin/activate
$ pip install -r requirements.txt
```

### 2.Training data
Prepare file of facial data of each person according to the structure:
```
train_img:
        /person1:
                /img1.jpg        
                /img2.jpg
                ...
        /person2:
                /img1.jpg
                /img2.jpg
                ...
        ...
 ```        
### 3. face detection and adjustment
After preparing the train data, we will proceed to detect faces, align and resize faces to homogenize one size.
```
python3 data_preprocess.py

```
### 4.Pre-trained models
| Model name| 	LFW accuracy | Training dataset|Architecture|
|--------------|-------|------|-------|
| [20180408-102900](https://drive.google.com/file/d/1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz/view) | 0.9905 | CASIA-WebFace | 	[Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
| [20180402-114759](https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view)| 0.9965 | VGGFace2 | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py)|

Download any model and extract it to `/model/`
### 4. Running training
```
python3 train_main.py
```
### 5. Facerecognition:
run file:
```
python3 facerecognition.py
```
The command will run by default with your webcam, if you want to change it to video, you can enter the video link

```
line13:
video= './class/2.mp4'# webcam '0'
```

https://user-images.githubusercontent.com/66860881/116190998-c428d080-a755-11eb-97c7-30b592948775.mp4

### 6.Get data from your webcam
###### 6.1. run the program and press `space` to take a picture, `esc` to exit
```
python3 data.py
```
###### 6.2.run the program will automatically take 20 pictures of the face
```
python3 get_faces_from_camera.py --face 20
