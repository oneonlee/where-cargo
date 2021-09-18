# 영상분석 방식을 통한 실시간 주차현황 확인 및 스마트 항만 주차정보시스템 구현

## <center>요약</center>

**어쩌구저쩌구**

---

## <center><strong>I. 서론</strong></center>

**어쩌구저쩌구**

---

<!-- ## <center>관련 연구</center>
**어쩌구저쩌구**

--- -->

## <center><strong>II. 설계 및 구현</strong></center>

### 1. 주차정보시스템

주차정보시스템이란 주차정보의 수집, 처리, 전달을 수행하고 주차장의 위치 및 주차장 상황에 관한 정보를 운전자에게 제공하여 빠른 주차장 찾기가 가능토록 지원해주는 시스템이다.<sup>[1]</sup> 주차정보를 수집하는 방식은 무선루프센서 방식, 초음파센서 방식, 영상분석 방식 등이 있다. **본 논문에서는 영상분석 방식을 통해 주차정보시스템을 구현하였다.**

### 2. 주차선 검출 및 주차면 구분

영상에서 에지(edge)는 한쪽 방향으로 픽셀 값이 급격하게 바뀌는 부분을 가리킨다. 즉, 어두운 영역에서 갑자기 밝아지거나 또는 밝은 영역에서 급격하게 어두워지는 부분을 말한다.<sup>[2]</sup>

일반적으로 주차장은 두께가 있는 흰색 실선을 통해 주차면을 나누는데, **본 연구에서는** 이 점을 착안하여 주차선 즉, 에지를 검출하고 각각의 주차면을 구분하였다.

에지를 검출하기에 앞서, 영상을 회색조(grayscale)로 변환하고, 가우시안 흐림(gaussian blur) 효과를 적용하여 영상을 **필터링**한다. 회색조 변환과 가우시안 흐림 효과를 적용함으로서 화소(pixel) 하나에 사용되는 데이터의 크기를 줄여 연산량과 연산속도를 낮출 수 있을 뿐만 아니라, 영상에 나타난 잡음(noise)을 처리하기에도 효과적이다.

전처리 과정을 거친 후, 대표적인 에지 검출 알고리즘인 Canny Edge Detection 알고리즘을 사용하여 경계선을 검출한다.

검출한 경계선을 모폴로지 연산(mprphological operation) 중 팽창(dilation) 기법을 적용하여 이미지를 팽창시키고, 이진화(binary) 시켜줌으로써 잡음을 제거하고 주차선의 구분을 명확하게 한다.

그 후, 영상의 모든 외곽선(contour)의 정보와 외곽선의 상하구조(hierachy)를 트리(tree) 계층으로 수집한다. 트리 계층의 상하구조에서 자식 노드(node)가 없는 것들만 외곽선을 나타냄으로서 주차면을 뽑아내고, 해당 영역들을 관심영역(ROI)으로 설정한다.

### 3. 차량의 주차 여부 판단

오픈 소스 머신러닝 라이브러리인 TensorFlow와 객체 탐지(object detection) 모델 중 딥 러닝(deep learning) 기반으로 실시간 객체 탐지(real-time object detection)가 가능한 알고리즘인 YOLOv4(You Only Look Once)<sup>[3]</sup>를 사용하여 차량의 주차 여부를 판단하였다.

아래 [그림 1]은 주차장에 주차된 차량들을 YOLOv4로 검출한 결과이다.

![그림 1](https://raw.githubusercontent.com/oneonlee/where-cargo/main/2021_smart_contest/%EC%B2%A8%EB%B6%80%ED%8C%8C%EC%9D%BC/%EC%BD%94%EB%93%9C%20%EB%B6%84%EC%84%9D%20%EA%B2%B0%EA%B3%BC/%E1%84%8C%E1%85%A1%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8E%E1%85%A1%E1%84%90%E1%85%A1%E1%86%B7%E1%84%8C%E1%85%B5%E1%84%8B%E1%85%A1%E1%86%AF%E1%84%80%E1%85%A9%E1%84%85%E1%85%B5%E1%84%8C%E1%85%B3%E1%86%B7-2.png)

<center>[그림 1] YOLOv4로 주차장 차량들을 검출한 결과</center>
<br>

**[그림 1]에서 확인할 수 있듯이** YOLOv4가 모든 차량에 대해 class를 정확하게 'car'라고 예측한 것을 확인할 수 있다. 예측한 class에 대한 신뢰도 및 확률을 나타내는 confidence score의 평균은 0.74로 YOLOv4가 적절한 정확도를 가진다는 것을 확인할 수 있다.

### 4. 웹 페이지 및 서버 구성

서버는 vultr의 호스팅 서비스를 이용해서 구현하였다. 운영체제는 우분투(ubuntu) 20.04를 이용했다. 웹 서버 구현을 위해서 nginx, 파이썬(python)의 장고(django), mariaDB를 사용했고, 효율적인 유지 보수를 위해서 도커시스템을 사용했다. **유저**가 한번 접속해서 오래 사용하는 방식이 아닌, 짧은 접속을 자주하는 웹 페이지이기 때문에, 새로 고침을 통해 새로운 정보를 조회 할 수 있고 최초 접속속도가 빠른 http 통신 방식으로 웹 페이지를 조회할 수 있도록 하였다. http 통신 과정에서의 기본적인 보안 시스템은 장고에서 제공되는 라이브러리들을 사용하였다.

![그림 2](https://raw.githubusercontent.com/oneonlee/where-cargo/main/2021_smart_contest/%EC%B2%A8%EB%B6%80%ED%8C%8C%EC%9D%BC/%EA%B5%AC%EC%84%B1%EB%8F%84%3A%ED%9D%90%EB%A6%84%EB%8F%84/%EC%84%9C%EB%B9%84%EC%8A%A4%20%EA%B5%AC%EC%84%B1%EB%8F%84.jpg)

<center>[그림 2] 서비스 구성도</center>
<br>

![그림 3](https://raw.githubusercontent.com/oneonlee/where-cargo/main/2021_smart_contest/%EC%B2%A8%EB%B6%80%ED%8C%8C%EC%9D%BC/%EA%B5%AC%EC%84%B1%EB%8F%84%3A%ED%9D%90%EB%A6%84%EB%8F%84/%EC%84%9C%EB%B9%84%EC%8A%A4%20%ED%9D%90%EB%A6%84%EB%8F%84.jpg)

<center>[그림 3] 서비스 흐름도</center>
<br>

---

## <center><strong>III. 실험</strong></center>

실험을 위하여, 아래 [그림 4]와 같이 모의 주차장을 제작하였다. 차량은 모형 자동차로 대체하였다.

![그림 4](https://github.com/oneonlee/where-cargo/blob/main/2021_smart_contest/%EC%B2%A8%EB%B6%80%ED%8C%8C%EC%9D%BC/%E1%84%8C%E1%85%AE%E1%84%8E%E1%85%A1%E1%84%8C%E1%85%A1%E1%86%BC2.png?raw=true)

<center>[그림 4] 모의 주차장</center>
<br>

[그림 4]와 같이 주차장에 차량이 주차되어 있을 때 카메라 클라이언트에서 차량 유무를 각 주차면마다 분석하고, 분석 데이터를 웹 서버로 보내어 [그림 5]와 같이 **웹 페이지에** 나타낸다.

![그림 5](https://github.com/oneonlee/where-cargo/blob/main/2021_smart_contest/%EC%B2%A8%EB%B6%80%ED%8C%8C%EC%9D%BC/%E1%84%8B%E1%85%B0%E1%86%B8.png?raw=true)

<center>[그림 5] 주차장 현황 안내 웹 페이지</center>
<br>
---

## <center><strong>IV. 결론</strong></center>

본 논문에서는 영상분석방식으로 주차정보를 분석하고, 운전자에게 실시간 주차현황을 제공함으로서 스마트 항만 주차정보시스템을 구현하였다.

**어쩌구저쩌구**

---

<br>

> ※ 본 논문은 과학기술정보통신부 정보통신창의인재양성사업의 지원을 통해 수행한 ICT멘토링 프로젝트 결과물입니다.

<br>

---

## <center><strong>참고문헌</strong></center>

[1] 손승녀, 조용성. "주차정보시스템 활성화 방안." _교통 기술과 정책 = Transportation technology and policy_ 13 no.2 (2016): 67.

[2] 황선규. OpenCV 4로 배우는 컴퓨터 비전과 머신 러닝. 서울: 길벗, 2019.

[3] Alexey Bochkovskiy, Chien-Yao Wang, and HongYuan Mark Liao. "Yolov4: Optimal speed and accuracy of object detection." _arXiv preprint arXiv_:2004.10934 (2020), https://arxiv.org/abs/2004.10934

---

#### 참고

1. **볼드친 부분은 약간 애매한 표현**
2. 서비스 구성도와 서비스 흐름도 배치 고민중
