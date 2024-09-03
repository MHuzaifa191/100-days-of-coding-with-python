import cv2
import numpy as np
import pyautogui

while True:
    image = pyautogui.screenshot(region=(700,260,150,150))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    black_pixels = np.sum(image < 100)
    white_pixels = np.sum(image > 100)

    print("white=", white_pixels, "; black=", black_pixels)

    # for light mode

    if black_pixels > 500 and black_pixels < 30000:
        print("jump1 white=", white_pixels, "; black=", black_pixels)
        pyautogui.press('up')
    if white_pixels > 500 and white_pixels < 30000:
     
        print("jump2 white=", white_pixels, "; black=", black_pixels)
        pyautogui.press('up')


    cv2.imshow('image', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break