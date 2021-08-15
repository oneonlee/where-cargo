import cv2
import numpy as np
import json
import time

def parking_slot_detection(): # 주차영역을 탐지하여 좌표를 반환
    print("WOW")

def region_of_interest(): # 탐지한 좌표를 바탕으로 관심영역을 설정하고, 관심영역 좌표를 반환
    print("WOW")

def car_detection(): # 영상에서 차를 탐지하고 차의 유무를 반환
    print("WOW")

def making_dict(): # 결과를 바탕으로 dict를 만드는 함수
    print("WOW")

    # result_dict example :

def update_json(result_dict): # result_dict를 입력받아 JSON 파일로 저장
    with open("data.json", "w") as f:
        json.dump(result_dict, f)

cap = cv2.VideoCapture(0) # 동영상 불러오기

while True:
    ret, image = cap.read()

    cv2.imshow('results',image) # 이미지 출력

    if cv2.waitKey(1) == ord('q'):
        break