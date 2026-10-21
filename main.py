#installations
from djitellopy import tello
from cvzone.PoseModule import PoseDetector
from mainPIDs import PIDs
import cv2 as cv
from time import sleep


#height and width
hi, wi = 480, 640

#PID values, change them to the values working for you
xPID = PIDs([0.30, 0, 0.05], wi//2)
yPID = PIDs([0.39, 0, 0.11], 310)
zPID = PIDs([0.0016, 0, 0.000013], 150000, limit=[-20, 15])


#tello connection
me = tello.Tello()
me.connect()
sleep(1)
print(me.get_battery())
sleep(1)
me.streamoff()
sleep(1)
me.streamon()
sleep(1)
me.takeoff()
sleep(1)
me.send_rc_control(0,0,15,0)
sleep(1.6)

detector = PoseDetector()


while True:
    img = me.get_frame_read().frame
    img = cv.resize(img, (640,480))
    img = detector.findPose(img, draw=False)
    lmList, bboxinfo = detector.findPosition(img, draw=False)


    xVal = 0
    yVal = 0
    zVal = 0

    if bboxinfo:
        cx, cy = bboxinfo['center']
        x, y, w, h = bboxinfo['bbox']
        area = w * h

        if lmList:
            upper_body_landmarks = [lmList[i] for i in [11, 12, 13, 14, 15, 16]]
            for lm in upper_body_landmarks:
                cv.circle(img, (lm[0], lm[1]), 10, -1)

        xVal = int(xPID.updatedV(cx))
        yVal = int(yPID.updatedV(cy))
        zVal = int(zPID.updatedV(area))

        me.send_rc_control(0, -zVal, -yVal, xVal)


    else:
        me.send_rc_control(0,0,0,0)


    cv.imshow('img', img)


    if cv.waitKey(5) & 0xFF == ord('q'):
        me.land()
        break

cv.destroyAllWindows()
