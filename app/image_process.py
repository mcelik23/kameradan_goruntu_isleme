import cv2

def renk_algilama(frame, config):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, config.red.lower, config.red.upper)
    yellow_mask = cv2.inRange(hsv, config.yellow.lower, config.yellow.upper)
    green_mask = cv2.inRange(hsv, config.green.lower, config.green.upper)

    return red_mask, yellow_mask, green_mask

def kontur_ciz(frame, mask, color, label):
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, color, 2)
            cv2.putText(frame, label, (center[0] - radius, center[1] - radius - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
