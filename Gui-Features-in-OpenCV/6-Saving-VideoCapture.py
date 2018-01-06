import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
output = cv2.VideoWriter('output.avi', fourcc, 60.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        frame = cv2.flip(frame, 0)

        output.write(frame)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()
