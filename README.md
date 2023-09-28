# WA_Coding_Challenge_Perception

WA CodingChallenge: Perception
![answer.png](https://github.com/dawn-cmd/WA_Coding_Challenge_Perception/blob/main/answer.png)

## Methodolgy

+ Detect cones in the picture by using hsv_pick.py.
  
![cone_pick](https://github.com/dawn-cmd/WA_Coding_Challenge_Perception/blob/main/cone_pick.png)

+ Separate them into two groups through the middle line.
+ Find the slope and intercept of two lines.
+ Draw the lines

## What did I try, and why did it not work?

+ I tried to use cv2.Canny to detect edges directly
+ But I find it always chooses the edge of tiles on the ground.

## Libraries

+ CV2 (Python)
+ Numpy (Python)
