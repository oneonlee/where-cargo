# 주차정보시스템 

## 기능
### 주차 현황 실시간 확인
#### 차량 검지 방법
- 영상분석 방식 (번호판 인식)
    - 검지영역	
        - 대당 3면
    - 장점	
        - 설치편리, 보안기능 포함
        - 검지영역의 설정 용이
    - 단점	
        - 환경영향 민감
        - 초기투자 비용 높음

- 영상분석 방식(점유방식)
    - 검지영역	
        - 대당 10 ~ 15면(이상조건)
    - 장점	
        - 설치편리, 비용 저렴
        - 검지영역의 설정 용이
    - 단점	
        - 주차면 카메라 설치 위치 영향 많음

- 초음파센서 방식
    - 검지영역	
        - 대당 1면
    - 장점	
        - 수집정보의 높은 신뢰도
        - 주차유도 가능
    - 단점	
        - 환경영향 민감
        - 시공방법의 비효율성

- 무선루프센서 방식
    - 검지영역	
        - 대당 1면
    - 장점	
        - 환경영향 없음
        - 간편한 설치
    - 단점	
        - 계수오차 발생
        - 유지관리비용 과다

#### 적용 기술
##### 영상처리
###### OpenCV를 통한 영상처리
- Algorithm
    1. (init) 비어있는 주차장의 사진의 차선을 인식하여 각각의 주차구역 및 검출영역을 설정한다.
    2. (count) 검출영역 중 주차구역 별로 차가 검출되면 그 주차구역에 count+=1
    3. (return) 결과값을 JSON 형식으로 return 한다.
    4. (repeat) 2번부터 3번까지의 과정을 5초마다 반복한다. 
    5. (sum) 한 개의 카메라 당 10~15개의 차량을 담당하고, 이미지 및 영상을 분석한 20개의 JSON 파일을 하나의 JSON 파일로 합쳐 프론트 및 백엔드에 전달한다.

- 알아야 할 것들
    - OpenCV 사용법
    - AWS 사용법
    - 소켓 프로그래밍 (Node.JS & Socket.io)

- 주차구역 검출 방법 연구
    1. 흰색 선 검출
    2. hough transform
    3. 직사각형 검출
###### 기타
- AWS Rekognition
- Firebase ML Kit
- Google Cloud Vision API

##### 적외선센서, 초음파센서 등 센서를 통한 차량 검지
    - 아두이노와 앱 간의 실시간 통신 방법 찾기
    
### 출차 시간 예측
#### 적용 기술
- 선형회귀

### 시간대별 예측 주차 빈자리 예측
- 직접 임의의 데이터를 만들어서 머신러닝
- Sk에너지 부장님한테 과거 주차장의 입출차 기록을 받을 수 있는지 여쭤보고 받았다면 그걸로 머신러닝

## 필요성
- 불법주정차 및 배회차량으로 인하여 교통체증과 같은 직접적인 교통문제 발생
- 주차장 검색 시간 및 주차 소요시간 증가로 인한 연료 낭비, 공해 발생 등
- 출처 : https://www.koreascience.or.kr/article/JAKO201620861242838.pdf
## 의의

## 애플리케이션
### 페이지
- 주차장 실시간 현황 확인
- 선박 or 터미널 작업 현황 확인
- 공지사항

#### 희망사항
- 위치정보
- 알림 
    - push
    - 알림톡