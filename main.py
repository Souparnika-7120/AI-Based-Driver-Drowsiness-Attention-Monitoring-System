import cv2
import datetime
import os

EYE_CLOSED_FRAMES = 15
eye_closed_counter = 0

# Create logs folder automatically if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

log_path = "logs/driver_log.csv"

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        # Draw eye rectangles
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.putText(frame, f"Eyes detected: {len(eyes)}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2)

        if len(eyes) == 0:
            eye_closed_counter += 1
        else:
            eye_closed_counter = 0

        # ALERT
        if eye_closed_counter > EYE_CLOSED_FRAMES:
            cv2.putText(frame, "DROWSINESS ALERT!",
                        (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        3)

            # Write to log
            with open(log_path, "a") as f:
                f.write(f"{datetime.datetime.now()},Drowsiness Detected\n")

    cv2.imshow("Driver Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
