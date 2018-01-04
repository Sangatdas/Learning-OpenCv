import cv2

cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame', gray)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release();
cv2.destroyAllWindows()