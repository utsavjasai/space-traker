# import cv2
# import pickle
# import cvzone
# import numpy as np

# # Video feed
# cap = cv2.VideoCapture('bikeparking.mp4')

# #for use cemera
# # cap = cv2.VideoCapture(0)
# with open('CarParkPos2', 'rb') as f:
#     posList = pickle.load(f)

# width, height = 107, 48


# def checkParkingSpace(imgPro):
#     spaceCounter = 0

#     for pos in posList:
#         x, y = pos

#         imgCrop = imgPro[y:y + height, x:x + width]
#         # cv2.imshow(str(x * y), imgCrop)
#         count = cv2.countNonZero(imgCrop)

#         if count < 900:
#             color = (0, 255, 0)
#             thickness = 5
#             spaceCounter += 1
#         else:
#             color = (0, 0, 255)
#             thickness = 2

#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
#         cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,thickness=2, offset=0, colorR=color)

#     cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,thickness=5, offset=20, colorR=(0, 200, 0))


# while True:

#     if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
#         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#     success, img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
#     imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 25, 16)
#     imgMedian = cv2.medianBlur(imgThreshold, 5)
#     kernel = np.ones((3, 3), np.uint8)
#     imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

#     checkParkingSpace(imgDilate)
#     cv2.imshow("Image", img)
#     # cv2.imshow("ImageBlur", imgBlur)
#     # cv2.imshow("ImageThres", imgMedian)
#     cv2.waitKey(1)


import cv2
import pickle
import cvzone
import numpy as np
import os

# Video feed
cap = cv2.VideoCapture('bikeparking.mp4')

# For use with camera
# cap = cv2.VideoCapture(0)

# Load parking positions
with open('CarParkPos2', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48

def get_next_filename(folder, base_name, extension):
    """
    Generate the next available filename in the specified folder.
    """
    i = 1
    while os.path.exists(os.path.join(folder, f"{base_name}{i}{extension}")):
        i += 1
    return os.path.join(folder, f"{base_name}{i}{extension}")

# Define folder and base name for recordings
folder = 'C:/Users/HP/Videos'
base_name = 'recording'
extension = '.mp4'

# Get the next available filename
output_path = get_next_filename(folder, base_name, extension)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # Release the current recording and start a new one
        out.release()
        output_path = get_next_filename(folder, base_name, extension)
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    if not success:
        break

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    
    # Write the frame into the file
    out.write(img)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
