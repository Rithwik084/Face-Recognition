import cv2
import numpy as np
import face_recognition
import os
import keyboard

path ="images"
Images = []
classnames = []
myList = os.listdir(path)

for cl in myList:
 curimage = cv2.imread(f'{path}/{cl}')
 Images.append(curimage)
 classnames.append(os.path.splitext(cl)[0])
print(classnames)

def findencodings(Images):
 Encodelist = []
 for Img in Images:
  Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
  encode = face_recognition.face_encodings(Img)[0]
  Encodelist.append(encode)
 return Encodelist
print("just a sec, encoding in progress")
encodelistknown = findencodings(Images)
print(" encoding complete")

print(len(encodelistknown))

cap = cv2.VideoCapture(0)

while True:
 if keyboard.is_pressed('esc'):
  exit()
 success, Img = cap.read()
 Imgsmall= cv2.resize(Img,(0,0),None,0.25,0.25)
 Imgsmall = cv2.cvtColor(Imgsmall, cv2.COLOR_BGR2RGB)
 faceincurframe = face_recognition.face_locations(Imgsmall)
 encodecurframe = face_recognition.face_encodings(Imgsmall,faceincurframe)

 for encodeface,faceloc in zip(encodecurframe,faceincurframe):
  matches = face_recognition.compare_faces(encodelistknown,encodeface)
  facedis = face_recognition.face_distance(encodelistknown,encodeface)
  print(facedis)
  matchindex = np.argmin(facedis)
  if matches[matchindex]:
   name = classnames[matchindex].upper()
   print(name)
   y1, x2, y2, x1 = faceloc
   y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
   cv2.rectangle(Img, (x1, y1), (x2, y2), (0, 255, 0), 2)
   cv2.rectangle(Img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
   cv2.putText(Img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

 cv2.imshow("webcam",Img)
 cv2.waitKey(1)
