#!/usr/bin/env python
import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='FAST feature detector tester.')
parser.add_argument("infile", help="input image")
parser.add_argument("--threshold", help="FAST threshold, default 12", type=int, default=12)
parser.add_argument("--test", help="make a test run", action="store_true")
parser.add_argument("--non-max-suppression", help="use non maximal suppression", action="store_true")

args = parser.parse_args()

def fast_and_save(infile, threshold, non_max_suppression):
    img = cv2.imread(infile,0)
    #We create the FAST object to detect edges
    fast_obj = cv2.FastFeatureDetector(
        threshold = threshold,
        nonmaxSuppression = 1 if non_max_suppression else 0
    )
    # fast_obj.setBool('nonmaxSuppression', 1 if non_max_suppression else 0)
    # find the keypoints

    kp = fast_obj.detect(img,None)
    # draw them in order to show them
    keypointImage = cv2.drawKeypoints(img, kp, color=(0,0,255))
    #save the result
    outfilename = 'fast_%s_%s.png' % (threshold,non_max_suppression)
    print outfilename
    cv2.imwrite(outfilename, keypointImage)

    return fast_obj, kp

if args.test :
    fast_and_save(args.infile, 8, True)
    fast_and_save(args.infile, 8, False)
    fast_and_save(args.infile, 10, True)
    fast_and_save(args.infile, 10, False)
    fast_and_save(args.infile, 12, True)
    fast_and_save(args.infile, 12, False)
    pass
else:
    fast_obj, keypoints = fast_and_save(args.infile, args.threshold, args.non_max_suppression)

    print "Threshold: ", fast_obj.getInt('threshold')
    print "nonmaxSuppression: ", fast_obj.getBool('nonmaxSuppression')
    print "Total Keypoints: ", len(keypoints)
