from PIL import Image
import numpy as np

with Image.open('images/birds.jpg') as img:
    img_arr = np.array(img)

imgFlipped_V_arr = img_arr[::-1]
imgFlipped_V = Image.fromarray(imgFlipped_V_arr)
imgFlipped_V.save('images/flippedV.jpg')

imgFlipped_H_arr = img_arr[:, ::-1]
imgFlipped_H = Image.fromarray(imgFlipped_H_arr)
imgFlipped_H.save('images/flippedH.jpg')

fixed_value = 40
imgB_arr = img_arr + fixed_value

for i in range(imgB_arr.shape[0]):
    for j in range(imgB_arr.shape[1]):
        for k in range(imgB_arr.shape[2]):
            if imgB_arr[i, j, k] > 255:
                imgB_arr[i, j, k] = 255

imgB = Image.fromarray(imgB_arr)
imgB.save('images/imgB.jpg')
imgMask_arr = img_arr
for i in range(310, 411):
    for j in range(310, 411):
        imgMask_arr[i, j, : ] = 0

imgMask = Image.fromarray(imgMask_arr)
imgMask.save('images/maskedImg.jpg')

