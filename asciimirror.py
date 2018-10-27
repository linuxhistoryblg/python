import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw, ImageOps

cap = cv2.VideoCapture(0)
#TOGGLE CHAR_LIST COMPLEXITY HERE#
#CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
CHAR_LIST = '@%#*+=-:. '
num_cols=100
font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=10)
bg_code=0
num_chars = len(CHAR_LIST)
print('PRESS q TO CLOSE THE OUTPUT WINDOW')
while(cap.isOpened()):
    ret, image = cap.read()
    if ret==True:
        image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        height, width = image.shape
        ##########################
        cell_width = width / 100
        cell_height = 2 * cell_width
        num_rows = int(height / cell_height)
        if num_cols > width or num_rows > height:
            print("Too many columns or rows. Use default setting")
            cell_width = 6
            cell_height = 12
            num_cols = int(width / cell_width)
            num_rows = int(height / cell_height)
        char_width, char_height = font.getsize("A")
        out_width = char_width * num_cols
        out_height = 2 * char_height * num_rows
        out_image = Image.new("L", (out_width, out_height), bg_code)
        draw = ImageDraw.Draw(out_image)
        for i in range(num_rows):
            line = "".join([CHAR_LIST[min(int(np.mean(
                image[int(i * cell_height):min(int((i + 1) * cell_height), height),
                int(j * cell_width):min(int((j + 1) * cell_width), width)]) * num_chars / 255), num_chars - 1)] for j in
                            range(num_cols)]) + "\n"
            
            
            draw.text((0, i * char_height), line, fill=255 - bg_code, font=font)
        cropped_image = out_image.getbbox()
        out_image = out_image.crop(cropped_image)
        out_image = cv2.cvtColor(np.array(out_image), cv2.COLOR_GRAY2BGR)
        out_image = np.array(out_image)
        
            
        #############################
        cv2.imshow("Look! You're in ascii",out_image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
