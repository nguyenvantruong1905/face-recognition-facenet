import sys
sys.path.append('../insightface/deploy')
sys.path.append('../insightface/common')

from mtcnn.mtcnn import MTCNN
from imutils import paths
from src import face_preprocess
import numpy as np
import argparse
import cv2
import os

ap = argparse.ArgumentParser()

ap.add_argument("--faces", default=20,
                help="Number of faces that camera will get")
ap.add_argument("--output", default="./train_img/unlabeled_faces",
                help="Path to faces output")

args = vars(ap.parse_args())

# Detector = mtcnn_detector
detector = MTCNN()
# initialize video stream
cap = cv2.VideoCapture(0)

# Setup some useful var
faces = 0
frames = 0
max_faces = int(args["faces"])
max_bbox = np.zeros(4)

while faces < max_faces:
    ret, frame = cap.read()
    frames += 1

    # Get all faces on current frame
    bboxes = detector.detect_faces(frame)

    if len(bboxes) != 0:
        # Get only the biggest face
        max_area = 0
        for bboxe in bboxes:
            bbox = bboxe["box"]
            bbox = np.array([bbox[0], bbox[1], bbox[0]+bbox[2], bbox[1]+bbox[3]])
            keypoints = bboxe["keypoints"]
            area = (bbox[2]-bbox[0])*(bbox[3]-bbox[1])
            if area > max_area:
                max_bbox = bbox
                landmarks = keypoints
                max_area = area

        max_bbox = max_bbox[0:4]


        # get each of 3 frames
        if frames%3 == 0:
            # convert to face_preprocess.preprocess input
            landmarks = np.array([landmarks["left_eye"][0], landmarks["right_eye"][0], landmarks["nose"][0], landmarks["mouth_left"][0], landmarks["mouth_right"][0],
                                 landmarks["left_eye"][1], landmarks["right_eye"][1], landmarks["nose"][1], landmarks["mouth_left"][1], landmarks["mouth_right"][1]])
            landmarks = landmarks.reshape((2,5)).T
            nimg = face_preprocess.preprocess(frame, max_bbox, landmarks, image_size='112,112')
            if not(os.path.exists(args["output"])):
                os.makedirs(args["output"])
            cv2.imwrite(os.path.join(args["output"], "{}.jpg".format(faces+1)), nimg)
            cv2.rectangle(frame, (max_bbox[0], max_bbox[1]), (max_bbox[2], max_bbox[3]), (255, 0, 0), 2)
            print("[INFO] {} faces detected".format(faces+1))
            faces += 1
    cv2.imshow("Face detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
