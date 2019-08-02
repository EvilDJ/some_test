import cv2
import numpy as np
import math
from 边缘检测 import sobel

img = cv2.imread('./11.jpg')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def non_maximum_suppression_default(dx,dy):
    #边缘强度
    # print(dx.shape,dy.shape)
    edgeMag = np.sqrt(np.power(dx,2.0)+np.power(dy,2.0))
    row,col = dx.shape
    gradientDirection = np.zeros(dx.shape)
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1,row-1):
        for c in range(1,col-1):
            angle = math.atan2(dy[r][c],dx[r][c])/math.pi*180
            gradientDirection[r][c] = angle
            #左
            if(abs(angle)<22.5 or abs(angle)>157.5):
                if(edgeMag[r][c]>edgeMag[r][c-1] and edgeMag[r][c]>edgeMag[r][c+1]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #左上，右下
            if (angle >= 22.5 and angle < 67.5 or (-angle > 112.5 and -angle<=157.5)):
                if (edgeMag[r][c] > edgeMag[r - 1][c - 1] and edgeMag[r][c] > edgeMag[r + 1][c + 1]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #上
            if (abs(angle) < 67.5 or abs(angle) > 112.5):
                if (edgeMag[r][c] > edgeMag[r - 1][c] and edgeMag[r][c] > edgeMag[r + 1][c]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #右上
            if (angle >112.5 and angle < 157.5 or (-angle >= 22.5 and -angle < 67.5)):
                if (edgeMag[r][c] > edgeMag[r - 1][c + 1] and edgeMag[r][c] > edgeMag[r + 1][c - 1]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup

def non_maximum_suppression_Inter(dx,dy):
    # 边缘强度
    edgeMag = np.sqrt(np.power(dx, 2.0) + np.power(dy, 2.0))
    r, c = dx.shape
    gradientDirection = np.zeros(dx.shape)
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for i in range(1,r-1):
        for j in range(1,c-1):
            if dy[r][c] == 0 and dx[r][c] == 0:
                continue
            angle = math.atan2(dy[r][c],dx[r][c])/math.pi*180
            gradientDirection[r][c] = angle
            #左
            if((angle > 45 and angle <= 90) or (angle > -135 and angle <= -90)):
                ration = dx[r][c]/dy[r][c]
                left_top = ration * edgeMag[r-1][c-1]+(1-ration)*edgeMag[r-1][c]
                right_bottom = (1-ration)*edgeMag[r+1][c]+ration*edgeMag[r+1][c+1]
                if edgeMag[r][c] > left_top and edgeMag[r][c] > right_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #左上，右下
            if ((angle > 90 and angle <= 135) or (angle > -90 and angle <= -45)):
                ration = dx[r][c] / dy[r][c]
                right_top = ration * edgeMag[r - 1][c + 1] + (1 - ration) * edgeMag[r - 1][c]
                left_bottom = ration * edgeMag[r + 1][c-1] + (1-ration) * edgeMag[r + 1][c]
                if edgeMag[r][c] > right_top and edgeMag[r][c] > left_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #上
            if ((angle > 0 and angle <= 45) or (angle > -180 and angle <= -135)):
                ration = dx[r][c] / dy[r][c]
                right_bottom = ration * edgeMag[r + 1][c + 1] + (1 - ration) * edgeMag[r][c + 1]
                left_top = ration * edgeMag[r - 1][c - 1] + (1-ration) * edgeMag[r][c-1]
                if edgeMag[r][c] > left_top and edgeMag[r][c] > right_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #右上
            if ((angle > 135 and angle <= 180) or (angle > -45 and angle <= 0)):
                ration = dx[r][c] / dy[r][c]
                right_top = ration * edgeMag[r - 1][c + 1] + (1 - ration) * edgeMag[r][c+1]
                left_bottom = ration * edgeMag[r + 1][c-1] + (1-ration) * edgeMag[r][c-1]
                if edgeMag[r][c] > right_top and edgeMag[r][c] > left_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup

def check(r,c,row,col):
    if r>=0 and r<row and c>=0 and c<col:
        return True
    else:return False

def trace(edgeMag_nonMaxSup,edge,lowerThresh,r,c,row,col):
    if edge[r][c] == 0:
        edge[r][c] = 255
        for i in range(-1,2):
            for j in range(-1,2):
                if check(r+i,c+j,row,col) and edgeMag_nonMaxSup[r+i][c+j] >= lowerThresh:
                    trace(edgeMag_nonMaxSup,edge,lowerThresh,r+i,c+j,row,col)

def hysteresisThreshold(edge_nonMaxSup,lowerThresh,uppperThresh):
    r,w = edge_nonMaxSup.shape
    edge = np.zeros(edge_nonMaxSup.shape,np.uint8)
    for i in range(1,r-1):
        for j in range(1,w -1):
            if edge_nonMaxSup[i][j]>=uppperThresh:
                trace(edge_nonMaxSup,edge,lowerThresh,i,j,r,w)
            if edge_nonMaxSup[i][j] < lowerThresh:
                edge[i][j] = 0
    return edge

#第一步
img_sobel_x,img_sobel_y = sobel.sobel(im,3)
#第二部
edge = np.sqrt(np.power(img_sobel_x,2.0)+np.power(img_sobel_y,2.0))
edge[edge>255] = 255
edge = edge.astype(np.uint8)
edge_SUP = non_maximum_suppression_default(img_sobel_x,img_sobel_y)
edge_SUP[edge_SUP>255] = 255
edge_SUP =edge_SUP.astype(np.uint8)
cv2.imshow('edge_',edge_SUP)
edge = hysteresisThreshold(edge_SUP,60,180)
lowerThresh = 40
upperThresh = 150
# edge = 255- edge
cv2.imshow('edge_canny',edge)
# cv2.imwrite('edge_canny.jpg',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()