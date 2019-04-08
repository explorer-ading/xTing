
import numpy as np
import cv2
from matplotlib import pyplot as plt

# https://stackoverflow.com/questions/50472180/match-two-images-keypoints

## Read the source image
img = cv2.imread('lena-465x465.jpg')
merge1 = np.concatenate((img1, img2), axis=0)
merge1 = np.concatenate((img1, img2), axis=0)
plt.imshow(cv2.cvtColor(merge1, cv2.COLOR_BGR2RGB))
plt.imshow(cv2.cvtColor(merge1, cv2.COLOR_BGR2RGB))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


## Create sample images
# upper 300pixels 
img1=img[:300]
# bottom 300pixels
img2=img[-300:]


## Direct merge vertically
# https://stackoverflow.com/questions/7589012/combining-two-images-with-opencv
merge1 = np.concatenate((img1, img2), axis=0)
plt.imshow(cv2.cvtColor(merge1, cv2.COLOR_BGR2RGB))
plt.show()



## Calculate the offset based on SIFT keypoints
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

#kpimg1=cv2.drawKeypoints(img1,kp1,kpimg1)
#plt.imshow(cv2.cvtColor(kpimg1, cv2.COLOR_BGR2RGB))
#kpimg2=cv2.drawKeypoints(img2,kp2,kpimg2)
#plt.imshow(cv2.cvtColor(kpimg2, cv2.COLOR_BGR2RGB))

# https://stackoverflow.com/questions/30807214/opencv-return-keypoints-coordinates-and-area-from-blob-detection-python
# https://docs.opencv.org/2.4/modules/features2d/doc/common_interfaces_of_feature_detectors.html#Point2f%20pt
match_kp = []
for i in range(len(des1)):
    for j in range(len(des2)):
        if (des1[i] == des2[j]).all():
            print(i,j)
            match_kp.append((i,j))

for p in match_kp:
    k1, k2 = p
    x1,y1,s1 = kp1[k1].pt[0],kp1[k1].pt[1],kp1[k1].size
    x2,y2,s2 = kp2[k2].pt[0],kp2[k2].pt[1],kp2[k2].size
    print("[%d,%d]%d;[%d,%d]%d;res[%d,%d]" %(x1,y1,s1,x2,y2,s2,x2-x1,y2-y1))


# As per the residual value of y2-y1, we can get the value 165(+/-1) .

merge2 = np.concatenate((img1[:165], img2), axis=0)
plt.imshow(cv2.cvtColor(merge2, cv2.COLOR_BGR2RGB))
plt.show()


