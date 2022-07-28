# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
# img1 = cv.imread('obama.jpg', cv.IMREAD_GRAYSCALE)
# img2 = cv.imread('obama2.jpg', cv.IMREAD_GRAYSCALE)
#
# orb = cv.ORB_create()
#
#
# kp1, des1 = orb.detectAndCompute(img1,None)
# kp2, des2 = orb.detectAndCompute(img2,None)
#
# bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# # Match descriptors.
# matches = bf.match(des1,des2)
# # Sort them in the order of their distance.
# matches = sorted(matches, key = lambda x:x.distance)
# # Draw first 10 matches.
# img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# plt.imshow(img3),plt.show()