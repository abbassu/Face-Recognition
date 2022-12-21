import numpy as np
import cv2
img = cv2.imread('inputImage.jpg')
facex = 0
facey = 0
facext = 0         
faceyt = 0
final_sx = []
final_sy = []
x_for_aim = []
y_for_aim = []
size_of_shape_x = []
size_of_shape_xtotal = []
size_of_shape_y = []
size_of_shape_ytotal = []
x_all = []
y_all = []
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 220, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.imshow("img", img)
for contour in contours:
    x99, y99, w99, h99 = cv2.boundingRect(contour)
    x_all.append(x99)
    y_all.append(y99)
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    if len(approx) == 2:
        ""
    elif len(approx) == 3:
        ""
    elif (len(approx) == 10 or len(approx) == 11 or len(approx) == 9):
        ""
    else:
        size_of_shape_x.append(x99)
        size_of_shape_xtotal.append(x99+w99)
        size_of_shape_y.append(y99)
        size_of_shape_ytotal.append(y99+h99)
for i in range((int(len(size_of_shape_ytotal)))-1):
    if(i > 0):
        if(size_of_shape_x[i] > size_of_shape_x[i-1]):
            size_of_shape_x.pop(i)
            size_of_shape_xtotal.pop(i)
            size_of_shape_y.pop(i)
            size_of_shape_ytotal.pop(i)
        elif(size_of_shape_x[i] == 0 and size_of_shape_y[i] == 0):
            size_of_shape_x.pop(i)
            size_of_shape_xtotal.pop(i)
            size_of_shape_y.pop(i)
            size_of_shape_ytotal.pop(i)
for j in range(int(len(size_of_shape_ytotal))):
    for i in range(int(len(x_all))):
        if(x_all[i] > size_of_shape_x[j] and x_all[i] < size_of_shape_xtotal[j]):
            if (y_all[i] > size_of_shape_y[j] and y_all[i] < size_of_shape_ytotal[j]):
                final_sx.append(x_all[i])
                final_sy.append(y_all[i])
                x_for_aim.append(size_of_shape_x[j])
                y_for_aim.append(size_of_shape_y[j])
facex = max(set(x_for_aim), key=x_for_aim.count)
facey = max(set(y_for_aim), key=y_for_aim.count)
for j in range(int(len(size_of_shape_ytotal))):
    if(size_of_shape_y[j] == facey):
        facext = size_of_shape_xtotal[j]
        faceyt = size_of_shape_ytotal[j]
final_sx.append(facex)
final_sy.append(facey)
for i in range(int(len(final_sx))):
    ""
for contour in contours:
    x99, y99, w99, h99 = cv2.boundingRect(contour)
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    xx, yy, hh, ww = cv2.boundingRect(contour)
    x = approx.ravel()[0]
    y = approx.ravel()[1]+50
    if len(approx) == 2:
        c = "Line"
        cv2.putText(img, c, (x+130, y),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 3:
        for i in range(int(len(final_sx))):
            if(xx in final_sx and yy in final_sy):
                break
            c = "Traingle"
            cv2.putText(img, c, (x+30, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif (len(approx) == 10 or len(approx) == 11 or len(approx) == 9):
        for i in range(int(len(final_sx))):
            if(xx in final_sx and yy in final_sy):
                break
            c = "Curve"
            cv2.putText(img, c, (x-60, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        for i in range(int(len(final_sx))):
            if(xx in final_sx and yy in final_sy):
                break
            c = "Rectangle"
            cv2.putText(img, c, (x-60, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        for i in range(int(len(final_sx))):
            if(xx in final_sx and yy in final_sy):
                break
            c = "Circle"
            cv2.putText(img, c, (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
eyeleft = int((faceyt-facey)/3)
eyeleft = eyeleft+40
eyeright = facex+490
nono = int(facey+((faceyt-facey)*2)/3)
cv2.putText(img, "Face", (facex+50, facey),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.putText(img, "Eye", (facex+70, facey+eyeleft),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.putText(img, "Eye", (facex+150, facey+eyeleft),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.putText(img, "Noise", (facex+80, nono),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.putText(img, "Mouth", (facex+80, faceyt-20),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
