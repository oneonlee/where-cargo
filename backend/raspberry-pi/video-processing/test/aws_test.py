import cv2
import json
import boto3
import time
start = time.time()  # 시작 시간 저장
 
def amazon_rekognition(image):
  Rekog = boto3.client('rekognition')

  h,w = image.shape[:2]
  regImg = cv2.resize(image, (int(0.2*w), int(0.2*h)))
  _, newjpeg = cv2.imencode('.jpg', regImg)
  imgbytes = newjpeg.tobytes()

  resp = Rekog.detect_labels(Image={'Bytes':imgbytes})

  return resp

def save_json(result_for_json):
    with open("data.json", "w") as f:
        json.dump(result_for_json, f)


# cap = cv2.VideoCapture("data/test2.mov")
cap = cv2.VideoCapture(0)
ret, img = cap.read() 

while cap.isOpened():
    ret, img = cap.read()     # 카메라로부터 현재 영상을 받아 img에 저장, 잘 받았다면 ret가 참

    if ret is False:
        break

    cv2.imshow

    resp = amazon_rekognition(img)

    for label_dict in resp["Labels"]:
          print(label_dict["Name"])
          if label_dict["Name"] == "Car":
                print("Car detected!")
                break
          elif label_dict["Name"] == "Vehicle":
                print("Vehicle detected!")
                break
          elif label_dict["Name"] == "Transportation":
                print("Transportation detected!")
                break
          elif label_dict["Name"] == "Toy":
                print("Toy detected!")
                break
      


    save_json(resp)

    cv2.imshow('result', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                       # 캡처 객체를 없애줌
cv2.destroyAllWindows()     

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
