# import cv2
# import pickle

# width, height = 50, 50

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

#     with open('CarParkPos', 'wb') as f:
#         pickle.dump(posList, f)


# while True:
#     img = cv2.imread('carParkImg.png')
#     for pos in posList:
#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

#     cv2.imshow("Image", img)
#     cv2.setMouseCallback("Image", mouseClick)
#     cv2.waitKey(1)




# import cv2
# import pickle

# a=int(input("enter the value of the box you want:"))
# b=int(input("enter the value of the box you want:"))


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

# # For laptop webcam
# # cap = cv2.VideoCapture(0)
# # cap = cv2.VideoCapture("C:/OneDrive/Desktop/Parking-Space-Counter-using-Machine-learning-main/bike.mp4")
# cap=cv2.imread("C:/OneDrive/Desktop/parking(assistent_utsav)/carParkImg.png")

# # For CCTV camera (replace <IP_ADDRESS> with the actual IP address of the camera)
# # cap = cv2.VideoCapture('http://<IP_ADDRESS>/video')

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     for pos in posList:
#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

#     cv2.imshow("Image", img)
#     cv2.setMouseCallback("Image", mouseClick)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()





import cv2
import pickle

a = int(input("Enter the value width of the box you want: "))
b = int(input("Enter the value hight of the box you want: "))

width, height = a, b

try:
    with open('CarParkPos2', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos2', 'wb') as f:
        pickle.dump(posList, f)

# Uncomment one of the following based on whether you are using a webcam, a video file, or an image

# For laptop webcam
# cap = cv2.VideoCapture(0)

# For video file
# cap = cv2.VideoCapture("C:/OneDrive/Desktop/Parking-Space-Counter-using-Machine-learning-main/bi85keparking.mp4")

# For a static image
cap = cv2.imread("C:/OneDrive/Desktop/parking(assistent_utsav)/parking2.jpg")

# Desired output dimensions
output_width = 775
output_height = 775

if isinstance(cap, cv2.VideoCapture):
    while True:
        success, img = cap.read()
        if not success:
            break

        img_resized = cv2.resize(img, (output_width, output_height))

        for pos in posList:
            cv2.rectangle(img_resized, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

        cv2.imshow("Image", img_resized)
        cv2.setMouseCallback("Image", mouseClick)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
else:
    img_resized = cv2.resize(cap, (output_width, output_height))
    while True:
        img_copy = img_resized.copy()
        for pos in posList:
            cv2.rectangle(img_copy, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

        cv2.imshow("Image", img_copy)
        cv2.setMouseCallback("Image", mouseClick)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
