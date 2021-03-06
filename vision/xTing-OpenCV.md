
## opencv
[](https://www.opencv.org/)

OpenCV (Open Source Computer Vision Library) is released under a BSD license and hence it’s free for both academic and commercial use. 
It has C++, Python and Java interfaces and supports Windows, Linux, Mac OS, iOS and Android. 
OpenCV was designed for computational efficiency and with a strong focus on real-time applications. Written in optimized C/C++, the library can take advantage of multi-core processing. 
Enabled with OpenCL, it can take advantage of the hardware acceleration of the underlying heterogeneous compute platform.

Adopted all around the world, OpenCV has more than 47 thousand people of user community and estimated number of downloads exceeding 14 million. 
Usage ranges from interactive art, to mines inspection, stitching maps on the web or through advanced robotics.

* [tutorial](https://docs.opencv.org/2.4/doc/tutorials/tutorials.html)
* [api-reference](https://docs.opencv.org/3.0-beta/modules/refman.html)


### install opencv on macos
* [install-opencv3-on-macos](https://www.learnopencv.com/install-opencv3-on-macos/)
* [install-on-macos](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/)

* my own experience :
`brew install opencv`

* verify the setup environment ;
`python3 -c 'import cv2; print(cv2.__version__);'`


### opencv-python
* [python-tutroals](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
* [official-tutorial](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)

* Video Analysis
* Camera Calibration and 3D Reconstruction

* Feature Detection 
	HAAR
	HOG
	SIFT
	SURF
	
* Machine Learning 
	KNN , cv2.KNearest()
	KMeans , cv2.kmeans()

	SVM 
	Random Forest 
	ANN 

* Computational Photography
	Image Denoising , Non-local Means Denoising algorithm to remove noise in the image.
	Image Inpainting , remove small noises, strokes etc in old photographs by a method called inpainting

* object detection (Haar Feature-based Cascade Classifiers which is achieved by Adaboost. ) 
	haarcascades , /usr/local/Cellar/opencv/4.0.1/share/opencv4/haarcascades
	`face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')`


### issues
* SFIT ;
[cant-use-surf-sift-in-opencv](https://stackoverflow.com/questions/18561910/cant-use-surf-sift-in-opencv)
	`sift = cv2.xfeatures2d.SIFT_create()`
