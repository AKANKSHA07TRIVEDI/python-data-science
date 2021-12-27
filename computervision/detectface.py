import cv2
cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('haarcascade.xml')

while True:
    #reading a single frame frame from capture point
    ret,frame = cap.read()
    faces = classifier.detectMultiScale(frame)
    for(x,y,w,h) in faces:
        cv2.cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    # displaying the frames in a window
    cv2.imshow('my webcam',frame)
    #for quitting the window on key press
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()