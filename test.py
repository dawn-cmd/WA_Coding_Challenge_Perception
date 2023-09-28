import cv2
import numpy as np


def process_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Decreased min Saturation, increased min Value
    lower_red1 = np.array([0, 173, 153])
    upper_red1 = np.array([180, 255, 255])
    # Decreased min Saturation, increased min Value
    lower_red2 = np.array([0, 173, 153])
    upper_red2 = np.array([180, 255, 255])

    # Threshold the image to keep only the red pixels
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Find contours in the mask
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process the detected contours
    left_points = []
    right_points = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        center_x = x + w // 2
        center_y = y + h // 2
        if center_x < img.shape[1] // 2:
            left_points.append((center_x, center_y))
        else:
            right_points.append((center_x, center_y))

    # Fit lines to the points using linear regression
    if left_points:
        left_slope, left_intercept = np.polyfit([p[0] for p in left_points], [
                                                p[1] for p in left_points], 1)
        cv2.line(img, (0, int(0 * left_slope + left_intercept)),
                 (img.shape[1], int(img.shape[1] * left_slope + left_intercept)), (0, 255, 0), 2)
    if right_points:
        right_slope, right_intercept = np.polyfit([p[0] for p in right_points], [
                                                  p[1] for p in right_points], 1)
        cv2.line(img, (0, int(0 * right_slope + right_intercept)),
                 (img.shape[1], int(img.shape[1] * right_slope + right_intercept)), (0, 255, 0), 2)

    # Save the result as 'answer.png'
    cv2.imwrite('answer.png', img)


# Call the function with the path to your image
process_image('red.png')
