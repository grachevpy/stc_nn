
import cv2  # собственно OpenCV
from pathlib import Path
import numpy as np  # для работы с математикой
import matplotlib.pyplot as plt # для вывода картинки

image_path = Path('C:\\', 'Users', 'maxgr', 'Desktop', 'marius.jpg')
image = cv2.imread(str(image_path), 1)
image_channels_reversed = image[:, :, ::-1]
plt.imshow(image_channels_reversed)
print("Image size is ", image.shape)

# выводим картинку
plt.show()

# focal_length = 0
# lens_distortion = 0
# camera_position_information = 0

