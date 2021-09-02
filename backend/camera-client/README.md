# 실시간 주차장 현황 분석 (모형)

영상 분석 방식으로 주차장의 주차 현황을 분석하여 웹으로 실시간 확인을 도와주는 프로젝트

## 사용 기술

- Python
- OpenCV
  - 사진 및 동영상 처리
  - Blur, Canny Edge, Dilate, Threshold 등 주차선을 검출하기 위한 전처리
  - findContours의 RETR_TREE 옵션으로 영상의 윤곽선을 트리 계층으로 검출
  - 검출한 주차 구역을 바탕으로 masking을 통한 관심구역 설정
- TensorFlow
- YOLOv4
  - Realtime Object Detection에 사용되는 알고리즘
- HTTP
  - requests 모듈을 활용하여 HTTP 중 POST 방식으로 서버에 주차 현황 분석 결과를 보냄
- ~~Amazon Rekognition~~
  - ~~클라우드를 기반으로 객체를 탐지할 수 있는 플랫폼~~
  - ~~YOLOv4에 비해 낮은 정확도로 사용중단~~
- ~~AWS SDK / Boto3~~
  - ~~Python용 AWS SDK로 Amazon Rekognition, Amazon S3 등 AWS 서비스를 API 방식으로 호출하여 사용~~

사용 동기, 장점 특점

## 개발환경

MacBook Pro 2020

```
!pip install opencv-python==4.5.2.54
<!-- !pip install lxml -->
<!-- !pip install tqdm -->
!pip install tensorflow==2.3.0rc0
<!-- !pip install absl-py -->
!pip install easydict
<!-- !pip install matplotlib -->
<!-- !pip install pillow
!pip install ten -->
!pip install requests
!pip install numpy
```

- [GitHub kairess | _tensorflow-yolov4-tflite_](https://github.com/kairess/tensorflow-yolov4-tflite)
- [GitHub hunglc007 | _tensorflow-yolov4-tflite_](https://github.com/hunglc007/tensorflow-yolov4-tflite)
- [GitHub niazahamd89 | _Cars-Detection-using-CascadeClassifier_](https://github.com/niazahamd89/Cars-Detection-using-CascadeClassifier)
- [GitHub sungw5 | _fullbody_car_detector_](https://github.com/sungw5/fullbody_car_detector)
- [GitHub andrewssobral | _vehicle_detection_haarcascades_](https://github.com/andrewssobral/vehicle_detection_haarcascades)
- [GitHub huhji | _licence_plate_recognition_korea_](https://github.com/huhji/licence_plate_recognition_korea)
- [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- [OpenCV 4.5.2 documentation](https://docs.opencv.org/4.5.2/)
- [Python 3.9.6 documentation](https://docs.python.org/3.9/)
- [YouTube 빵형의 개발도상국 | _사물인식 YOLO v4 실습하는 영상_](https://www.youtube.com/watch?v=hxwEqXCgQO4)
- [Youtube Amazon Web Services Korea | _AWS 머신러닝 서비스를 활용한 실시간 이미지 분석 - 김무현 (AWS 솔루션즈 아키텍트)_](https://www.youtube.com/watch?v=sieD-8l9Cgw)
- [Youtube Amazon Web Services Korea | _Amazon Rekognition으로 나만의 컴퓨터 비전 서비스 만들기 – 권신중:: AWS Innovate 2021_](https://www.youtube.com/watch?v=tioJru6b_4M)
- [네이버 블로그 windowsub0406 | _[Udacity] SelfDrivingCar- 2-0. 차선 인식_](https://blog.naver.com/windowsub0406/220893187693)
- [스파르타코딩클럽 | _이미지처리로 시작하는 딥러닝_](https://spartacodingclub.kr/online/dl)
- [윤대희. 2019. _C#과 파이썬을 활용한 OpenCV 4 프로그래밍._ 위키북스.](https://wikibook.co.kr/opencv4/)
- [김동근. 2018. _python으로 배우는 OpenCV 프로그래밍._ 가메출판사.](https://www.kame.co.kr/nkm/detail.php?tcode=308&tbook_jong=3)
