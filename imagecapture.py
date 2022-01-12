import cv2
import numpy as np

cap = cv2.VideoCapture(1)
i =0
while (True):

    # Take each frame

    _, frame= cap.read()


    cv2.imshow('Result', frame)
    frame = np.copy(frame)
    if cv2.waitKey(20) & 0xFF == ord('t'):

        cv2.imwrite(f"images\\img_{i}.jpg", frame)
        i+=1
    elif cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

