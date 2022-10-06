from email.mime import image
from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import torch
from time import time
import numpy as np


# Create your views here.

# 웹사이트로 보내는 요청을 핸들링하는 함수를 정의
def cctv_main(request):
    return render(request, 'cctv_cam/cctv_main.html')


def video_feed(request):
    ob = ObjectDetection()
    return StreamingHttpResponse(ob.stream(), content_type='multipart/x-mixed-replace;boundary=frame')


# 이거를 사용해야 함
class ObjectDetection:
    # YouTube 동영상에 YOLOv5 구현
    def __init__(self):
        # 객체 생성 시 호출
        # url: 예측 대상 YouTube URL
        # out_file: 유효한 출력 파일 이름 *.avi

        self.model = self.load_model()
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def get_video_from_url(self):
        return cv2.VideoCapture(0)

    def load_model(self):
        # YOLOv5 모델 로드
        model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5s', classes=2)
        return model

    def score_frame(self, frame):
        # frame: 단일 프레임; numpy/list/tuple 형식
        # return: 프레임에서 모델이 감지한 객체의 레이블과 좌표
        self.model.to(self.device)
        frame = [frame]
        # result cf) # 54th line "results.xyxyn[0]" result
        #      xmin      ymin     xmax     ymax     confidence     class     name
        # 0   749.50    43.50    1148.0   704.5      0.874023          0   person
        # 1   433.50   433.50     517.5   714.5      0.687988         27      tie
        # 2   114.75   195.75    1095.0   708.0      0.624512          0   person
        # 3   986.00   304.00    1028.0   420.0      0.286865         27      tie
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1].cpu().numpy(), results.xyxyn[0][:, :-1].cpu().numpy()
        return labels, cord

    def class_to_label(self, x):
        # x 숫자 레이블 -> 문자열 레이블로 반환
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        # 경계상자와 레이블을 프레임에 플로팅
        # results: 프레임에서 모델이 감지한 객체의 레이블과 좌표
        # frame: 점수화된 프레임
        # return: 경계 상자와 레이블이 플로팅된 프레임
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.6:
                alarm()
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                    row[3] * y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, f"{i}"
                            + ': ' + str(x1) + ', ' + str(x2) + ', ' + str(y1) + ', ' + str(y2),
                            (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        return frame

    def stream(self):
        # 인스턴스 생성 시 호출; 프레임 단위로 비디오 로드
        cap = self.get_video_from_url()
        while True:
            ret, frame = cap.read()
            if not ret:
                print(f" 비디오 캡쳐 오류")
                break
            # 캡쳐한 이미지를 브라우저로 보내기 위해서 바이트화 시켜준다.
            start_time = time()
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)
            image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
            end_time = time()
            fps = 1 / np.round(end_time - start_time, 3)
            print(f"Frames Per Second : {fps}")
            # yield를 사용하여 generator를 반환 iter와 유사
            # generator는 반환 값을 모두 메모리에 올리지 않고 즉석으로 하나씩 반환
            # b'' 바이트 형으로 문자열 입력
            # while 문에 넣었다는 것은 조건을 만족할 때까지 다음의 값을 불러오기 위해 사용하였다.
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')


# Create your views here.
import winsound
import threading

def beepsound():
    # 알림음 재생
    for _ in range(3):
        winsound.Beep(
            frequency=1000,  # Hz
            duration=100  # milliseconds
        )
        winsound.Beep(
            frequency=500,  # Hz
            duration=100  # milliseconds
        )
        winsound.Beep(
            frequency=2000,  # Hz
            duration=100  # milliseconds
        )


def alarm():
    t = threading.Thread(target=beepsound, args=())
    t.start()
