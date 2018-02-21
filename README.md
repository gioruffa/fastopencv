# FAST Feature Detection Alogrithm

test script for evaluation the FAST openCV implementation.

```
usage: image.py [-h] [--threshold THRESHOLD] [--test] [--non-max-suppression] infile

FAST feature detector tester.

positional arguments:
  infile                input image

optional arguments:
  -h, --help            show this help message and exit
  --threshold THRESHOLD
                        FAST threshold, default 12
  --test                make a test run
  --non-max-suppression
                        use non maximal suppression
```

## Test run
The test run will create 6 output images toggling the threshold and the nonmaxSuppression parameter
