import cv2
import numpy as np


def judging_continous(CONTINOUS_VALUE, detected_result_dict, continous_info):

    for i in range(len(continous_info)):
        if detected_result_dict[i] == 0:
            continous_info[i] += 1
            if continous_info[i] < CONTINOUS_VALUE:
                detected_result_dict[i] = 1
            elif continous_info[i] > CONTINOUS_VALUE*2:  # 스택오버플로우 방지
                continous_info[i] = CONTINOUS_VALUE
        else:
            continous_info[i] = 0

    return detected_result_dict


# def save_json(result_for_json):
#     with open("data.json", "w") as f:
#         json.dump(result_for_json, f)


def roi_setting(img, idx, contour):
    mask = np.zeros_like(img, dtype='uint8')
    mask = cv2.drawContours(mask, contour, idx, (1, 1, 1), -1)
    seprated_slot_img = img * mask

    return seprated_slot_img


def parking_slot_detection(init_img):  # return parking_slot_dict
    init_img_gray = cv2.cvtColor(init_img, cv2.COLOR_BGR2GRAY)

    blur_img = cv2.GaussianBlur(init_img_gray, (11, 11), 0)  # Blur 효과

    canny_img = cv2.Canny(blur_img, 70, 210)  # Canny edge 알고리즘

    kernel = np.ones((5, 5), np.uint8)
    dilated_img = cv2.dilate(canny_img, kernel, iterations=1)

    # 바이너리 이미지로 변환
    ret, imthres = cv2.threshold(dilated_img, 100, 255, cv2.THRESH_BINARY)

    # cv2.imshow('img', imthres)

    # 모든 컨투어를 트리 계층 으로 수집
    contour, hierarchy = cv2.findContours(
        imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected_slot_img = np.zeros_like(init_img, dtype='uint8')
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

    cv2.imwrite("detection.jpg", detected_slot_img)

    cv2.imshow(f"총 주차면 수 : {len(parking_slot_dict)}면", detected_slot_img)

    return parking_slot_dict, contour


def init_img_capture(img):
    print("Processing \"init.png\" file ...")
    # time.sleep(1)
    cv2.imwrite("init.png", img)  # 파일이름(한글안됨), 이미지
    print("Done!")
