from functions import *

import cv2
import detect_simple as detect
from http_client import http_client

URL = "http://192.168.0.16:8080/result/"


cap = cv2.VideoCapture("data/test3.mov")
# cap = cv2.VideoCapture(1)
ret, img = cap.read()     # 카메라로부터 현재 영상을 받아 img에 저장, 잘 받았다면 ret가 참

init_img_capture(img)

init_img = cv2.imread('init.png')
parking_slot_dict, contour = parking_slot_detection(init_img)
print(f"총 주차 면 : {len(parking_slot_dict)}")

count = 0
CONTINOUS_VALUE = 3
continous_info = [CONTINOUS_VALUE +
                  1 for i in range(len(parking_slot_dict))]

# 무한루프
while cap.isOpened():
    cap.set(cv2.CAP_PROP_POS_FRAMES, count*70)
    ret, img = cap.read()     # 카메라로부터 현재 영상을 받아 img에 저장, 잘 받았다면 ret가 참

    if ret is False:
        break

    detected_obj_list = []

    detected_result_dict = {}
    for key in range(len(parking_slot_dict)):
        detected_result_dict[key] = 0
    i = 0
    for idx in parking_slot_dict:
        seprated_slot_img = roi_setting(img, idx, contour)
        parking_slot_dict[idx] = seprated_slot_img

        cv2.imshow(f'{idx}', parking_slot_dict[idx])
        detected_obj_list = detect.detect(
            parking_slot_dict[idx], detected_obj_list)

        if len(detected_obj_list) > 0:
            detected_result_dict[i] = 1
            print(detected_obj_list)

        i += 1

    result_dict_for_json = judging_continous(
        CONTINOUS_VALUE, detected_result_dict, continous_info)
    print(result_dict_for_json)
    http_client(result_dict_for_json, URL)

    cv2.imshow('result', img)

    count += 1

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                       # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌
