import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture('bikeparking.mp4')

with open('CarParkPos2', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,thickness=5, offset=20, colorR=(0, 200, 0))


while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThres", imgMedian)
    cv2.waitKey(10)


# import cv2
# import pytesseract

# # Function to recognize number plates
# def recognize_number_plate(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Use bilateral filter to remove noise and keep edge sharp
#     gray = cv2.bilateralFilter(gray, 11, 17, 17)
    
#     # Detect edges in the image
#     edged = cv2.Canny(gray, 170, 200)
    
#     # Find contours based on edges detected
#     contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]
    
#     # Initialize number plate contour and ROI
#     number_plate_contour = None
#     x, y, w, h = 0, 0, 0, 0

#     # Loop over contours to find number plate
#     for contour in contours:
#         approx = cv2.approxPolyDP(contour, 10, True)
#         if len(approx) == 4:  # Number plate contour should have 4 sides
#             number_plate_contour = approx
#             x, y, w, h = cv2.boundingRect(contour)
#             break

#     # Extract the number plate from the image
#     number_plate = gray[y:y+h, x:x+w]
    
#     # Use Tesseract to do OCR on the number plate
#     text = pytesseract.image_to_string(number_plate, config='--psm 8')
    
#     return text, number_plate

# # Test the function
# if __name__ == "__main__":
#     image = cv2.imread('path_to_your_test_image.jpg')
#     text, number_plate_image = recognize_number_plate(image)
#     print(f"Detected Number Plate Text: {text}")
#     cv2.imshow("Number Plate", number_plate_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# ##for add image in this code###########


# import cv2
# import pickle

# a = int(input("Enter the value of the box width you want: "))
# b = int(input("Enter the value of the box height you want: "))

# width, height = a, b

# try:
#     with open('CarParkPos2', 'rb') as f:
#         posList = pickle.load(f)
# except:
#     posList = []

# def mouseClick(events, x, y, flags, params):
#     if events == cv2.EVENT_LBUTTONDOWN:
#         posList.append((x, y))
#     if events == cv2.EVENT_RBUTTONDOWN:
#         for i, pos in enumerate(posList):
#             x1, y1 = pos
#             if x1 < x < x1 + width and y1 < y < y1 + height:
#                 posList.pop(i)

#     with open('CarParkPos2', 'wb') as f:
#         pickle.dump(posList, f)

# # Read the image
# img = cv2.imread("C:/OneDrive/Desktop/parking(assistent_utsav)/carParkImg.png")

# while True:
#     # Copy the image to draw rectangles on it
#     img_copy = img.copy()

#     for pos in posList:
#         cv2.rectangle(img_copy, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

#     cv2.imshow("Image", img_copy)
#     cv2.setMouseCallback("Image", mouseClick)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()
