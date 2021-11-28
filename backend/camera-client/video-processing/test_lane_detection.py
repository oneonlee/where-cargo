import cv2
import numpy as np


cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('data/test.mov')
ret, img = cap.read()

while cap.isOpened():
    ret, img = cap.read()     # 카메라로부터 현재 영상을 받아 img에 저장, 잘 받았다면 ret가 참

    if ret is False:
        break

    init_img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur_img = cv2.GaussianBlur(init_img_gray, (11, 11), 0)  # Blur 효과

    canny_img = cv2.Canny(blur_img, 70, 210)  # Canny edge 알고리즘

    kernel = np.ones((5, 5), np.uint8)
    dilated_img = cv2.dilate(canny_img, kernel, iterations=1)

    # 바이너리 이미지로 변환
    ret, imthres = cv2.threshold(dilated_img, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow('img', imthres)

    # 모든 컨투어를 트리 계층 으로 수집
    contour, hierarchy = cv2.findContours(
        imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected_slot_img = np.zeros_like(img, dtype='uint8')
    parking_slot_dict = {}

    # 부모노드가 있는 것들만 (외곽이 아닌 것들만) 컨투어 그리기
    # 0818 수정 : 자식 노드가 없는 것만 컨투어 그리기
    for idx, cont in enumerate(contour):
        if hierarchy[0][idx][2] == -1:
            cv2.drawContours(detected_slot_img, contour,
                             idx, (255, 255, 255), 5)

            parking_slot_dict[idx] = None

            # 컨투어 첫 좌표에 인덱스 숫자 표시
            cv2.putText(detected_slot_img, str(idx), tuple(
                cont[0][0]), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255))
    print(f"{len(parking_slot_dict)}")
    cv2.imwrite("detection.jpg", detected_slot_img)

    cv2.imshow(f"총 주차면 수 : {len(parking_slot_dict)}면", detected_slot_img)

    cv2.imshow('result', img)

    if cv2.waitKey(1) == ord('q'):
        break
