from YOLO_Model import head_body_detection_model
from ultralytics import YOLO
import cv2
import numpy as np



if __name__ == "__main__":
    input_data_path = "data/input_1/img_991.jpg"
    model_path = "YOLO_Model/best.pt"
    model_1 = head_body_detection_model.HeadBodyClassifier(input_img_path=input_data_path, model_path = model_path)
    out_file = model_1.get_head_body_vector()
    head_img = out_file["head"]
    body_img = out_file["body"]

    head_body_detection_model.show_img(head_img)
    head_body_detection_model.show_img(body_img)




