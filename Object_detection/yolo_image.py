import cv2
from ultralytics import YOLO

model =YOLO("yolov8n.pt")

video_path = 0
cap = cv2.VideoCapture(vide_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame, verbose = False)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO video Detection", annotated_frame)
    if cv2waitkey(1) & 0xFF ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()