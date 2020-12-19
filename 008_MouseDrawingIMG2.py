import cv2
import numpy as np

# VARIABELS

# True while mouse button down, False while mouse button UP
drawing = False
ix = -1
iy = -1


# FUNCTION
def draw_rectangle(event,x,y,flags,params):
    global  ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix,iy = x,y # 실제 마우스가 어디에 있는지 좌표값

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0)-1)


# SHOWING THE IMAGE


# BLACK

img = np.zeros((512,512,3,))

cv2.namedWindow(winname="test")

cv2.setMouseCallback("test",draw_rectangle) # 콜백마우스를 draw_rectangle 함수에적용


while True:

    cv2.imshow("test",img)

    if cv2.waitKey(1) & 0xFF == 27 : # esc 아스키코드
        break

cv2.destroyWindow()